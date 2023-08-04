# Week5
## Task3
~~~~sql
INSERT INTO member (name, username, password, follower_count) VALUES ("test", "test", "test", 13);
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_1.jpg)

~~~~sql
SELECT * FROM member;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_1.jpg)

~~~~sql
SELECT * FROM member ORDER BY time DESC;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_2.jpg)

~~~~sql
SELECT * FROM member ORDER BY time DESC limit 1,3;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_3.jpg)

~~~~sql
SELECT * FROM member WHERE username = "test";
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_4.jpg)

~~~~sql
SELECT * FROM member WHERE username = "test" AND password = "test";
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_5.jpg)

~~~~sql
UPDATE member SET name = "test2" WHERE username = "test";
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task3_6.jpg)

## Task4
~~~~sql
SELECT COUNT(id) FROM member;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task4_1.jpg)

~~~~sql
SELECT SUM(follower_count) FROM member;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task4_2.jpg)

~~~~sql
SELECT AVG(follower_count) FROM member;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task4_3.jpg)

## Task5
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task5_1.jpg)
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task5_1_sub.jpg)

~~~~sql
SELECT message.content, member.username FROM member INNER JOIN message ON message.member_id=member.id;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task5_2.jpg)

~~~~sql
SELECT message.content, member.username, member.name FROM message INNER JOIN member ON message.member_id=member.id AND member.username="test";
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task5_3.jpg)

~~~~sql
SELECT AVG(message.like_count) AS "AVG(like_count)", member.username, member.name
    FROM member INNER JOIN message 
    ON message.member_id=member.id AND member.username="test"
    GROUP BY member.name;
~~~~
![image](https://github.com/c20kyo1827/c20kyo1827.github.io/blob/main/week5/cmd%20image/task5_4.jpg)