CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (id, role, name, email, phone, password_hash)
VALUES (
'1',
  'admin',
  'Admin User',
  'admin@mcd.in',
  '1234567890',
  'scrypt:32768:8:1$fzZQH4O2Okf0c50Z$9cd6ffe3b348e3b453e1255a6158ea72a5be0b46945bf0f102d70ae8dcc40904d95eacb368281f18eb5f922ffb5b2b2b22aadd9240e4c7bae5a41de501f007a5'
);


DELETE FROM users
WHERE email = 'hari@hr.in';

SELECT * FROM users


INSERT INTO users (role, name, email, phone, password_hash)
VALUES (
  'HR',
  'Hari',
  'hari@hr.in',
  '9999999999',
  'scrypt:32768:8:1$rCuPtZgwWPfWSnLp$928b4b33c7fa95a9d880a733a88f6eb13d75beaef735e29edd231290a3696d7268fa217c42e14a94f55eeb8ee0151bf4ab233429dde217ccfd05d372cea38a34'
);
