# Question 2 — Simple Employee File Management

## Problem Statement

Build a small Python application that stores employee details (Employee ID, Name, Role, Salary) in a file called `employees.txt`, reads them back, and prints a simple report:

- all employees
- employees whose salary is greater than ₹50,000
- the employee with the highest salary
- the number of employees in each role

## Approach / Logic

1. **Employee class:** `Employee` stores `employee_id`, `name`, `role` and `salary`, which are set in the constructor (`__init__`). It has a `display_details()` method that prints one employee, and a `to_line()` helper that formats the record for the file.
2. **File handling:** All file access uses a context manager (`with open(...)`), so the file is always closed.
   - `add_employee()` appends one record to `employees.txt`.
   - `read_employees()` reads the file line by line, splits each line on commas and creates an `Employee` object. Any line that cannot be parsed raises a `ValueError`, which is caught; the line is skipped and a message is printed.
3. **Exception handling:** `main()` calls `read_employees()` inside a `try` block. If `employees.txt` does not exist, the `FileNotFoundError` is caught, the file is created with sample data through `add_employee()`, and then it is read again.
4. **Report functions:**
   - `find_employees_above_salary()` uses a list comprehension to return employees earning more than ₹50,000.
   - `find_highest_salary()` uses `max()` with a `key` function.
   - `find_employees_by_role()` builds a dictionary of role → count.
5. **Output:** Roles are printed in alphabetical order.

## How to Run

```bash
cd question2
python main.py
```

Requires Python 3.6 or later. No external packages are needed.

The program finds `employees.txt` in the same folder as `main.py`, so it also works when you run it from another directory. To see the missing-file handling, delete or rename `employees.txt` and run the program again; the file is created again from the sample data.

> **Windows note:** If the `₹` symbol does not print correctly in your terminal, run `set PYTHONIOENCODING=utf-8` (cmd) or `$env:PYTHONIOENCODING="utf-8"` (PowerShell) first.

## Sample Input (`employees.txt`)

```
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
```

## Sample Output

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

When `employees.txt` is missing, this line is printed before the report:

```
'employees.txt' not found. Creating it with sample data...
```

## Python Concepts Used

| Concept                | Where it is used                                                         |
|------------------------|--------------------------------------------------------------------------|
| Class & object         | `Employee` class; one object per record                                  |
| Constructor & method   | `__init__()`, `display_details()`, `to_line()`                           |
| File handling          | Append mode in `add_employee()`, read mode in `read_employees()`         |
| Context manager        | `with open(...) as file:`                                                |
| Exception handling     | `FileNotFoundError` in `main()`, `ValueError` for invalid lines          |
| Functions              | `add_employee()`, `read_employees()`, `find_highest_salary()`, `find_employees_by_role()`, `find_employees_above_salary()` |
| Lists                  | List of `Employee` objects                                               |
| Dictionaries           | Role → count in `find_employees_by_role()`                               |
| List comprehension     | `find_employees_above_salary()`                                          |
| Built-ins              | `max()` with `lambda`, `sorted()`, `enumerate()`                         |
