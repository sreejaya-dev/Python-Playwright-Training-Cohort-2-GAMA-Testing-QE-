# Python Milestone Assessment

This milestone assessment tests basic Python programming through two small, practical tasks.

## Structure

```
python-milestone-assessment/
│
├── question1/
│   ├── main.py          # Student Marks Management System
│   └── README.md
│
├── question2/
│   ├── main.py          # Simple Employee File Management
│   ├── employees.txt    # Employee data file
│   └── README.md
│
└── README.md
```

## Problem Statement

**Question 1: Student Marks Management System.** Accept details of multiple students (ID, Name, Python, SQL and AI marks). Calculate each student's Total, Average, Grade and PASS/FAIL result (PASS if the average is 40 or more). Display the student with the highest average and the students whose average is above 75.

**Question 2: Simple Employee File Management.** Store employee details (ID, Name, Role, Salary) in `employees.txt`, read them back, and report all employees, employees earning more than ₹50,000, the highest-paid employee, and the number of employees in each role. Use an `Employee` class, a context manager, and exception handling for a missing file.

## Approach / Logic

| Question | Approach |
|----------|----------|
| 1 | Each student is a dictionary with a nested `marks` dictionary, and all students are kept in a list. Separate functions calculate the total, average, grade and result. A loop finds the highest average, and a list comprehension collects students averaging above 75. |
| 2 | An `Employee` class holds each record. `add_employee()` and `read_employees()` use `with open()` to work with `employees.txt`. A `FileNotFoundError` is caught and the file is recreated from sample data. Report functions filter by salary, find the maximum salary, and count employees per role with a dictionary. |

See each question's README for full details.

## How to Run

You need Python 3.6 or later. No external packages are required.

```bash
# Question 1
cd question1
python main.py

# Question 2
cd question2
python main.py
```

## Sample Input

**Question 1:** Answer `y` to use the built-in sample data, or `n` to enter students yourself:

```
Use sample student data? (y/n): n
Enter number of students: 1

Enter details of student 1
  Student ID: 101
  Student Name: Rahul
  Python Marks: 85
  SQL Marks: 75
  AI Marks: 80
```

**Question 2:** `employees.txt`

```
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
```

## Sample Output

**Question 1** (shortened; the full output is in [question1/README.md](question1/README.md))

```
===== Student Result =====
Student ID   : 101
Name         : Rahul
Python Marks : 85
SQL Marks    : 75
AI Marks     : 80
Total        : 240
Average      : 80
Grade        : A
Result       : PASS
--------------------------
...

Highest Scoring Student: Rahul (Average: 80)
Students above 75: Rahul, Priya
```

**Question 2**

```
===== Employee Details =====
101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====
John - ₹60000

Highest Paid Employee: John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
```

## Python Concepts Used

| Question | Concepts |
|----------|----------|
| 1 | Lists, dictionaries (nested), functions, `if/elif/else`, conditional expressions, `for` and `while` loops, list comprehension, dict comprehension, f-string formatting |
| 2 | Class and object, constructor (`__init__`) and methods, file handling (read and append), context manager (`with open()`), exception handling (`FileNotFoundError`, `ValueError`), lists, dictionaries, list comprehension, `max()` with `lambda`, `sorted()`, `enumerate()` |
