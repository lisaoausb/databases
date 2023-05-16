
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

DROP SEQUENCE IF EXISTS comments_id_seq;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text 
);
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content text,
    author text,
    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

INSERT INTO posts (title, content) VALUES('title1', 'content1');
INSERT INTO posts (title, content) VALUES('title2', 'content2');
INSERT INTO posts (title, content) VALUES('title3', 'content3');
INSERT INTO comments (content, author, post_id) VALUES('comment1', 'author1', 2);
INSERT INTO comments (content, author, post_id) VALUES('comment2', 'author2', 1);
INSERT INTO comments (content, author, post_id) VALUES('comment3', 'author2', 3);
INSERT INTO comments (content, author, post_id) VALUES('comment4', 'author2', 2);
INSERT INTO comments (content, author, post_id) VALUES('comment5', 'author3', 2);
INSERT INTO comments (content, author, post_id) VALUES('comment6', 'author4', 1);
INSERT INTO comments (content, author, post_id) VALUES('comment7', 'author1', 3);
INSERT INTO comments (content, author, post_id) VALUES('comment8', 'author5', 2);