-- 01
SELECT * FROM users;

-- 02
SELECT id, username FROM users;

-- 03
SELECT * FROM users WHERE username = 'alice';

-- 04
SELECT * FROM users WHERE id >= 2;

-- 05
SELECT * FROM users ORDER BY created_at DESC;

-- 06
SELECT * FROM users LIMIT 2;

-- 07
INSERT INTO users (username, email)
VALUES ('test_user', 'test@example.com');

-- 08
UPDATE users
SET email = 'test_new@example.com'
WHERE username = 'test_user';

-- 09
DELETE FROM users
WHERE username = 'test_user';

-- 10
SELECT
    u.username,
    d.title
FROM users u
JOIN documents d
    ON u.id = d.user_id;

-- 11
SELECT
    u.username,
    s.title
FROM users u
JOIN sessions s
    ON u.id = s.user_id;

-- 12
SELECT
    u.username,
    s.title,
    m.role,
    m.content
FROM users u
JOIN sessions s
    ON u.id = s.user_id
JOIN messages m
    ON s.id = m.session_id;

-- 13
SELECT
    u.username,
    s.title
FROM users u
LEFT JOIN sessions s
    ON u.id = s.user_id;

-- 14
SELECT
    user_id,
    COUNT(*) AS session_count
FROM sessions
GROUP BY user_id;

-- 15
SELECT
    user_id,
    COUNT(*) AS session_count
FROM sessions
GROUP BY user_id
HAVING COUNT(*) >= 1;

-- 16
WITH session_counts AS (
    SELECT
        user_id,
        COUNT(*) AS session_count
    FROM sessions
    GROUP BY user_id
)
SELECT *
FROM session_counts;

-- 17
SELECT
    session_id,
    content,
    ROW_NUMBER() OVER (
        PARTITION BY session_id
        ORDER BY created_at
    ) AS message_no
FROM messages;

-- 18
SELECT
    session_id,
    content,
    LAG(content) OVER (
        PARTITION BY session_id
        ORDER BY created_at
    ) AS previous_message
FROM messages;

-- 19
SELECT
    user_id,
    title,
    ROW_NUMBER() OVER (
        PARTITION BY user_id
        ORDER BY created_at DESC
    ) AS rn
FROM sessions;

-- 20
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE username = 'alice';