"""
Question 2 - Simple Employee File Management
Stores employee details in a file, reads them back and generates a simple report.
"""

import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employees.txt")
SALARY_LIMIT = 50000

SAMPLE_EMPLOYEES = [
    (101, "Rahul", "Python Developer", 50000),
    (102, "Anjali", "Tester", 45000),
    (103, "John", "Developer", 60000),
    (104, "Priya", "Tester", 48000),
]


class Employee:
    """Represents a single employee"""

    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        """Print the employee details in a single line"""
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")

    def to_line(self):
        """Return the employee as a comma separated line for the file"""
        return f"{self.employee_id},{self.name},{self.role},{self.salary}\n"


def add_employee(employee, file_name=FILE_NAME):
    """Append an employee record to the file"""
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(employee.to_line())


def read_employees(file_name=FILE_NAME):
    """Read employees from the file and return a list of Employee objects"""
    employees = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                employee_id, name, role, salary = line.split(",")
                employees.append(Employee(int(employee_id), name.strip(), role.strip(), int(salary)))
            except ValueError:
                print(f"Skipping invalid record on line {line_number}: {line}")
    return employees


def create_sample_file(file_name=FILE_NAME):
    """Create the employee file with sample data"""
    for employee_id, name, role, salary in SAMPLE_EMPLOYEES:
        add_employee(Employee(employee_id, name, role, salary), file_name)


def display_all_employees(employees):
    """Display details of every employee"""
    print("===== Employee Details =====")
    for employee in employees:
        employee.display_details()


def find_employees_above_salary(employees, limit=SALARY_LIMIT):
    """Return employees whose salary is greater than the given limit"""
    return [employee for employee in employees if employee.salary > limit]


def find_highest_salary(employees):
    """Return the employee with the highest salary"""
    return max(employees, key=lambda employee: employee.salary)


def find_employees_by_role(employees):
    """Return a dictionary with the count of employees in each role"""
    role_count = {}
    for employee in employees:
        role_count[employee.role] = role_count.get(employee.role, 0) + 1
    return role_count


def main():
    try:
        employees = read_employees()
    except FileNotFoundError:
        print(f"'{os.path.basename(FILE_NAME)}' not found. Creating it with sample data...\n")
        create_sample_file()
        employees = read_employees()

    if not employees:
        print("No employee records found.")
        return

    display_all_employees(employees)

    print(f"\n===== Employees with Salary > {SALARY_LIMIT} =====")
    high_earners = find_employees_above_salary(employees)
    if high_earners:
        for employee in high_earners:
            print(f"{employee.name} - ₹{employee.salary}")
    else:
        print("None")

    highest = find_highest_salary(employees)
    print(f"\nHighest Paid Employee: {highest.name} - ₹{highest.salary}")

    print("\nEmployee Count by Role:")
    for role, count in sorted(find_employees_by_role(employees).items()):
        print(f"{role}: {count}")


if __name__ == "__main__":
    main()
