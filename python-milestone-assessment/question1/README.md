# Question 1 — Student Marks Management System

## Problem Statement

Develop a Python program that accepts details of multiple students (Student ID, Name, Python, SQL and AI marks), calculates each student's Total, Average and Grade, shows whether they PASS or FAIL, and displays a summary with the highest-scoring student and the students who averaged above 75.

## Approach / Logic

1. **Input:** The program asks if you want to use the built-in sample data. If you answer `n`, it asks how many students there are and then reads each student's details. Marks are checked so that only whole numbers from 0 to 100 are accepted.
2. **Storage:** Each student is a dictionary (`id`, `name`, `marks`), where `marks` is itself a dictionary keyed by subject. All students are kept in a list.
3. **Calculations** (in `process_students()`):
   - Total = sum of the three subject marks
   - Average = Total / number of subjects (rounded to 2 decimals)
   - Grade:

     | Average | Grade |
     |---------|-------|
     | >= 75   | A     |
     | >= 60   | B     |
     | >= 50   | C     |
     | >= 40   | D     |
     | < 40    | F     |

   - Result = `PASS` if Average >= 40, otherwise `FAIL`
4. **Summary:**
   - `find_highest_scorer()` loops through the students to find the highest average.
   - `find_top_performers()` uses a **list comprehension** to collect the names of students with an average above 75.
5. **Output:** `display_results()` prints each student's result in aligned columns, followed by the summary.

## How to Run

```bash
cd question1
python main.py
```

Requires Python 3.6 or later. No external packages are needed.

## Sample Input

```
Use sample student data? (y/n): n
Enter number of students: 2

Enter details of student 1
  Student ID: 101
  Student Name: Rahul
  Python Marks: 85
  SQL Marks: 75
  AI Marks: 80

Enter details of student 2
  Student ID: 102
  Student Name: Anjali
  Python Marks: 60
  SQL Marks: 70
  AI Marks: 65
```

Built-in sample data (used when you answer `y`):

| ID  | Name   | Python | SQL | AI |
|-----|--------|--------|-----|----|
| 101 | Rahul  | 85     | 75  | 80 |
| 102 | Anjali | 60     | 70  | 65 |
| 103 | Priya  | 78     | 74  | 80 |
| 104 | Arun   | 30     | 35  | 40 |

## Sample Output (built-in sample data)

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
Student ID   : 102
Name         : Anjali
Python Marks : 60
SQL Marks    : 70
AI Marks     : 65
Total        : 195
Average      : 65
Grade        : B
Result       : PASS
--------------------------
Student ID   : 103
Name         : Priya
Python Marks : 78
SQL Marks    : 74
AI Marks     : 80
Total        : 232
Average      : 77.33
Grade        : A
Result       : PASS
--------------------------
Student ID   : 104
Name         : Arun
Python Marks : 30
SQL Marks    : 35
AI Marks     : 40
Total        : 105
Average      : 35
Grade        : F
Result       : FAIL
--------------------------

Highest Scoring Student: Rahul (Average: 80)
Students above 75: Rahul, Priya
```

## Python Concepts Used

| Concept               | Where it is used                                                              |
|-----------------------|-------------------------------------------------------------------------------|
| Lists                 | `SUBJECTS`, the list of student records                                       |
| Dictionaries          | Each student record and its nested `marks` dictionary                         |
| Functions             | `calculate_total()`, `calculate_average()`, `calculate_grade()`, `get_result()`, `find_highest_scorer()`, `find_top_performers()`, `display_results()` |
| Conditional statements| `if / elif / else` in `calculate_grade()`, conditional expression in `get_result()` |
| Loops                 | `for` loops over students and subjects, `while` loops for input validation    |
| List comprehension    | `find_top_performers()`                                                       |
| Dict comprehension    | Reading marks for every subject in `accept_students()`                        |
| f-strings / formatting| Aligned output in `display_results()`                                         |
| `__main__` guard      | `if __name__ == "__main__": main()`                                           |
