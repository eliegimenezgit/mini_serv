use epytodo
CREATE TABLE user(user_id INT PRIMARY KEY NOT NULL, username VARCHAR(10) NOT NULL, password VARCHAR(10) NOT NULL);
CREATE TABLE task(task_id INT PRIMARY KEY NOT NULL, title VARCHAR(10) NOT NULL, begin DATETIME, end DATETIME, status INT);
CREATE TABLE user_has_task(fk_user_id INT, fk_task_id INT);