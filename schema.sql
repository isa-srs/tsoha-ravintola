CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users,
    name TEXT,
    cuisine TEXT
);
