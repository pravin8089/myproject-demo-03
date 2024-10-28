-- DROP Table if exists 
drop table if exists employees ;

-- Create employees table
CREATE TABLE employees (
    id INT AUTOINCREMENT PRIMARY KEY,
    first_name STRING,
    last_name STRING,
    email STRING,
    hire_date DATE
);

-- Insert records into employees table
INSERT INTO employees (first_name, last_name, email, hire_date) VALUES 
('John', 'Doe', 'john.doe@example.com', '2022-01-15'),
('Jane', 'Smith', 'jane.smith@example.com', '2021-07-22'),
('Alice', 'Johnson', 'alice.johnson@example.com', '2020-11-01');

