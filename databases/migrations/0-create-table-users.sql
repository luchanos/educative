CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    name TEXT,
    surname text,
    unique_code text unique
);
