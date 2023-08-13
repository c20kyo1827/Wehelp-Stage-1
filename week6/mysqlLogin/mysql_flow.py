import mysql.connector
import argparse
import json
import os

class mysql_flow:
    def __init__(self):
        self._mydb = None

    def reset(self):
        self.connect()
        self.reset_database()
        self.reset_table()

    def init(self):
        self.connect()
        mycursor = self._mydb.cursor()
        mycursor.execute("USE website")

    def connect(self):
        root_file_path = os.path.join("D:\\", "Temp", "Wehelp", "c20kyo1827.github.io", "week6", "mysqlLogin", "root.json")
        with open(root_file_path, "r") as f:
            root_info = json.load(f)
            self._mydb= mysql.connector.connect(
                host=root_info["host"],
                user=root_info["user"],
                password=root_info["password"]
            )

    def reset_database(self):
        if self._mydb==None:
            return
        mycursor = self._mydb.cursor()
        mycursor.execute("DROP DATABASE IF EXISTS website")
        mycursor.execute("CREATE DATABASE website")
        mycursor.execute("USE website")

    def reset_table(self):
        if self._mydb==None:
            return
        mycursor = self._mydb.cursor()
        mycursor.execute("DROP TABLE IF EXISTS message")
        mycursor.execute("DROP TABLE IF EXISTS member")
        mycursor.execute( \
            "CREATE TABLE member( \
                id bigint AUTO_INCREMENT, \
                name varchar(255) NOT NULL, \
                username varchar(255) NOT NULL, \
                password varchar(255) NOT NULL, \
                follower_count int UNSIGNED NOT NULL DEFAULT 0, \
                time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, \
                PRIMARY KEY(id) \
            )" \
        )
        mycursor.execute( \
            "CREATE TABLE message( \
                id bigint AUTO_INCREMENT, \
                member_id bigint NOT NULL, \
                content varchar(255) NOT NULL, \
                like_count int UNSIGNED NOT NULL DEFAULT 0, \
                time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, \
                PRIMARY KEY(id), \
                FOREIGN KEY(member_id) REFERENCES member(id) \
            )" \
        )
    
    def show(self):
        mycursor = self._mydb.cursor()
        mycursor.execute("SELECT * FROM member")
        member_info = mycursor.fetchall()
        for x in member_info: print(x)
        mycursor.execute("SELECT * FROM message")
        message_info = mycursor.fetchall()
        for x in message_info: print(x)

    def get_member(self, username, password=None):
        mycursor = self._mydb.cursor()
        if password==None:
            sql = "SELECT id, username, name FROM member WHERE username = %s"
            val = (username, )
        else:
            sql = "SELECT id, username, name FROM member WHERE username = %s AND password = %s"
            val = (username, password)
        mycursor.execute(sql, val)
        return mycursor.fetchall()

    def add_member(self, name, username, password, follower_count=0):
        mycursor = self._mydb.cursor()
        sql = "INSERT INTO member (name, username, password, follower_count) VALUES (%s, %s, %s, %s)"
        val = (name, username, password, follower_count)
        mycursor.execute(sql, val)
        self._mydb.commit()

    def get_message(self):
        mycursor = self._mydb.cursor()
        mycursor.execute("SELECT message.id, message.content, member.username FROM member INNER JOIN message ON message.member_id=member.id ORDER BY message.time DESC")
        message_info = mycursor.fetchall()
        return message_info

    def add_message(self, member_id, content, like_count=0):
        mycursor = self._mydb.cursor()
        sql = "INSERT INTO message (member_id, content, like_count) SELECT id, %s, %s FROM member WHERE id=%s LIMIT 1"
        val = (content, like_count, member_id)
        mycursor.execute(sql, val)
        self._mydb.commit()
    
    def delete_message(self, id):
        mycursor = self._mydb.cursor()
        sql = "DELETE FROM message WHERE id=%s"
        val = (id,)
        mycursor.execute(sql, val)
        self._mydb.commit()


if __name__=="__main__":
    flow = mysql_flow()
    reset = input("Do you want to reset : ")
    if reset=="yes":
        flow.reset()
    else:
        flow.init()

    flow.show()