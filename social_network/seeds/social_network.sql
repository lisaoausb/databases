
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_seq;
DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_seq;

CREATE SEQUENCE IF NOT EXISTS user_accounts_seq;
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE SEQUENCE IF NOT EXISTS posts_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (email_address, username) VALUES ('test@gmail.com', 'test');
INSERT INTO user_accounts (email_address, username) VALUES ('seed@gmail.com', 'seed');
INSERT INTO user_accounts (email_address, username) VALUES ('social@gmail.com', 'social');

INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('title', 'content', 30, 2);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('titel', 'inhalt', 2, 2);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('titre', 'contenue', 1038, 1);