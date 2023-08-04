#====================================================
SELECT "Reset the website database" AS "Message";
    DROP DATABASE IF EXISTS website;
#====================================================
SELECT "Task 2" AS "Message";
    CREATE DATABASE website;
SELECT "Create the website database" AS "Message";
    USE website;
SELECT "Reset the message table" AS "Message";
    DROP TABLE IF EXISTS message;
SELECT "Reset the member table" AS "Message";
    DROP TABLE IF EXISTS member;
    SHOW FULL TABLES;
SELECT "Create the member table" AS "Message";
    CREATE TABLE member(
        id bigint AUTO_INCREMENT,
        name varchar(255) NOT NULL,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL,
        follower_count int UNSIGNED NOT NULL DEFAULT 0,
        time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id)
    );
#====================================================
SELECT "Task 3" AS "Message";
    SELECT "Insert data into member table" AS "Message";
    INSERT INTO member (name, username, password, follower_count) VALUES ("test", "test", "test", 13);
    SELECT SLEEP(3);
    INSERT INTO member (name, username, password, follower_count) VALUES ("user4", "user4", "user4_passwd", 17);
    SELECT SLEEP(3);
    INSERT INTO member (name, username, password, follower_count) VALUES ("user1", "user1", "user1_passwd", 11);
    SELECT SLEEP(3);
    INSERT INTO member (name, username, password, follower_count) VALUES ("user2", "user2", "user2_passwd", 21);
    SELECT SLEEP(3);
    INSERT INTO member (name, username, password, follower_count) VALUES ("user3", "user3", "user3_passwd", 44);
    SELECT * FROM member;
    SELECT * FROM member ORDER BY time DESC;
    SELECT * FROM member ORDER BY time DESC limit 1,3;
    SELECT * FROM member WHERE username = "test";
    SELECT * FROM member WHERE username = "test" AND password = "test";
    UPDATE member SET name = "test2" WHERE username = "test";
    SELECT * FROM member;
#====================================================
SELECT "Task 4" AS "Message";
    SELECT COUNT(id) FROM member;
    SELECT SUM(follower_count) FROM member;
    SELECT AVG(follower_count) FROM member;
#====================================================
SELECT "Task 5" AS "Message";
SELECT "Create the message table" AS "Message";
    CREATE TABLE message(
        id bigint AUTO_INCREMENT,
        member_id bigint NOT NULL,
        content varchar(255) NOT NULL,
        like_count int UNSIGNED NOT NULL DEFAULT 0,
        time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        FOREIGN KEY(member_id) REFERENCES member(id)
    );
    SELECT "Insert data into message table" AS "Message";
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is test. #1", 1 FROM member WHERE id=1 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #1", 7 FROM member WHERE id=2 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is test. #2", 3 FROM member WHERE id=1 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #5", 4 FROM member WHERE id=5 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #3", 1 FROM member WHERE id=4 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #4", 9 FROM member WHERE id=4 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is test. #3", 11 FROM member WHERE id=1 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #6", 12 FROM member WHERE id=5 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #2", 22 FROM member WHERE id=3 LIMIT 1;
    SELECT SLEEP(3);
    INSERT INTO message (member_id, content, like_count) SELECT id, "This is user. #7", 13 FROM member WHERE id=5 LIMIT 1;
    SELECT * FROM message;
    SELECT message.content, member.username FROM member INNER JOIN message ON message.member_id=member.id;
    SELECT message.content, member.username, member.name FROM message INNER JOIN member ON message.member_id=member.id AND member.username="test";
    SELECT AVG(message.like_count) AS "AVG(like_count)", member.username, member.name
        FROM member INNER JOIN message 
        ON message.member_id=member.id AND member.username="test"
        GROUP BY member.name;
    /*
        In window cmd to dump data.sql
        mysqldump -u root -p website > D:\Temp\Wehelp\c20kyo1827.github.io\week5\data.sql
    */