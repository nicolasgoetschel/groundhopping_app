DROP TABLE IF EXISTS grounds;
DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    flag VARCHAR(255)
);

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    logo VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    tier INT
);

CREATE TABLE grounds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team VARCHAR(255),
    location VARCHAR(255),
    capacity INT,
    visited BOOLEAN,
    league_id INT NOT NULL REFERENCES leagues(id) ON DELETE CASCADE
);


