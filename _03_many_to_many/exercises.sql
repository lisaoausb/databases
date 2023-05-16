-- exercise:

SELECT posts.id, posts.title
  FROM posts 
    JOIN posts_tags ON posts_tags.post_id = posts.id
    JOIN tags ON posts_tags.tag_id = tags.id
    WHERE tags.name = 'travel';

-- challenge:

-- to add new tag to table
INSERT INTO tags (name) VALUES ('sql') RETURNING id;

-- to associate post with new tag
INSERT INTO posts_tags (post_id, tag_id) VALUES (7, 5);

-- to verify it worked: return all posts associated with new tag
SELECT posts.title FROM posts 
JOIN posts_tags ON posts_tags.post_id = posts.id
JOIN tags ON tags.id = posts_tags.tag_id
WHERE tags.name = 'sql';
