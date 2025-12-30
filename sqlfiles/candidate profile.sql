CREATE TABLE candidate_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    dob DATE,
    address TEXT,
    category TEXT,
    education TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO candidate_profiles (dob, address, category, education, created_at)

SELECT * FROM candidate_profiles