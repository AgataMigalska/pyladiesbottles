DROP TABLE IF EXISTS POSTS;
CREATE TABLE POSTS (
    ID MEDIUMINT NOT NULL AUTO_INCREMENT,
    TITLE VARCHAR(100),
    CONTENT TEXT,
    AUTHOR VARCHAR(100),
    POST_DATE DATETIME,
    PRIMARY KEY (ID)
);