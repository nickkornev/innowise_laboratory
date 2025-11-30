-- Command 1: create tables 'students' and 'grades'.
-- Create table 'students'.

CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name TEXT NOT NULL,
birth_year INTEGER NOT NULL
)

-- Create table 'grades'.

CREATE TABLE IF NOT EXISTS grades(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
subject TEXT NOT NULL,
grade INTEGER CHECK(grade >= 1 and grade <= 100),
FOREIGN KEY (student_id) REFERENCES students(id)
)


-- Command 2: insert data.
-- Insert data into table 'students'.

INSERT INTO students(full_name, birth_year)
VALUES
   ('Alice Johnson', 2005),
   ('Brian Smith', 2004),
   ('Carla Reyes', 2009),
   ('Daniel Kim', 2005),
   ('Eva Thompson', 2003),
   ('Felix Nguyen', 2007),
   ('Grace Patel', 2005),
   ('Henry Lopez', 2004),
   ('Isabella Martinez', 2006)

-- Insert data into table 'grades'.

INSERT INTO grades(student_id, subject, grade)
VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 72),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92)


-- Command 3: find all grades for a specific student (Alice Johnson).

SELECT student_id, full_name, subject, grade
FROM
    students JOIN grades
    on students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson'


-- Command 4: calculate the average grade per student.

SELECT student_id, full_name, ROUND(AVG(grade),2) AS average_grade
FROM
    students JOIN grades
    on students.id = grades.student_id
GROUP BY full_name
ORDER BY full_name


-- Command 5: list all students born after 2004.

SELECT * FROM students
WHERE birth_year > 2004
ORDER BY full_name


-- Command 6: create a query that lists all subjects and their average grade.

SELECT subject, ROUND(AVG(grade),2) AS average_grade
FROM grades
GROUP BY subject
ORDER BY subject


-- Command 7: find top 3 students with the highest average grades.

SELECT student_id, full_name, ROUND(AVG(grade),2) AS average_grade
FROM
    students JOIN grades
    on students.id = grades.student_id
GROUP BY full_name
ORDER BY average_grade DESC
LIMIT 3


-- Command 8: show all students who have scored below 80 in any subject.

SELECT student_id, full_name, subject, grade
FROM
    students JOIN grades
    on students.id = grades.student_id
WHERE grade < 80









