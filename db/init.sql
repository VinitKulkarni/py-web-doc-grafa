CREATE DATABASE IF NOT EXISTS project_db;

USE project_db;

CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255),
    manager VARCHAR(255),
    developer VARCHAR(255),
    tester VARCHAR(255),
    start_date DATE,
    end_date DATE,
    notes TEXT
);
