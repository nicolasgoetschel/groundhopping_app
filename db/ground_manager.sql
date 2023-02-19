DROP TABLE IF EXISTS grounds;
DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS countries;

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    flag VARCHAR(8)
);

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    logo VARCHAR(255)
);

CREATE TABLE grounds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team VARCHAR(255),
    location VARCHAR(255),
    capacity INT,
    visited BOOLEAN
);