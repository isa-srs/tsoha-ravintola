CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users,
    name TEXT,
    cuisine TEXT
);

CREATE TABLE schedules (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    opens_at TEXT,
    closes_at TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    stars INTEGER,
    comment TEXT,
    posted_at TIMESTAMP DEFAULT Now()
);

CREATE TABLE favourites (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    restaurant_id INTEGER REFERENCES restaurants
);
