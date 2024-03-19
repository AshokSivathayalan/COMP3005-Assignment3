CREATE TABLE students(student_id SERIAL PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(30), email VARCHAR(50), enrollment_date DATE);
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');