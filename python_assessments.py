"""
Python Assessment Solutions
Complete coverage of all parts: fundamentals, functions, file handling, and OOP
"""

# ============================================================================
# PART 1: PYTHON FUNDAMENTALS 
# ============================================================================

print("=" * 70)
print("PART 1: PYTHON FUNDAMENTALS")
print("=" * 70)

# Question 1: First largest number
print("\n--- Question 1: First Largest Number ---")
numbers = [12, 5, 8, 20, 15]
largest = max(numbers)
print(f"List: {numbers}")
print(f"First largest number: {largest}")

# Question 2: Character frequency
print("\n--- Question 2: Character Frequency ---")
string = 'programming'
char_freq = {}
for char in string:
    char_freq[char] = char_freq.get(char, 0) + 1
print(f"String: '{string}'")
print(f"Character frequency: {char_freq}")

# Question 3: Student marks analysis
print("\n--- Question 3: Student Marks Analysis ---")
students = {
    "Alice": 85,
    "Bob": 35,
    "Charlie": 42
}
print("Student Results:")
for student, marks in students.items():
    result = "Pass" if marks >= 40 else "Fail"
    print(f"  {student}: {marks} - {result}")


# ============================================================================
# PART 2: FUNCTIONS 
# ============================================================================

print("\n" + "=" * 70)
print("PART 2: FUNCTIONS")
print("=" * 70)

# Question 6: Function with return value
print("\n--- Question 6: Calculate Bill with Discount ---")
def calculate_bill(price, quantity):
    """Calculate total bill with 10% discount if amount exceeds ₹2000"""
    total = price * quantity
    if total > 2000:
        discount = total * 0.10
        total = total - discount
    return total

result1 = calculate_bill(500, 5)
print(f"calculate_bill(500, 5) = {result1}")
print(f"Expected: 2250.0")

result2 = calculate_bill(400, 5)
print(f"calculate_bill(400, 5) = {result2}")

result3 = calculate_bill(300, 10)
print(f"calculate_bill(300, 10) = {result3}")


# Question 7: Lambda function
print("\n--- Question 7: Lambda Function ---")
numbers = [12, 5, 18, 7, 24, 9, 30]
multiplied = list(map(lambda x: x * 3, numbers))
print(f"Original list: {numbers}")
print(f"After multiplying by 3: {multiplied}")


# Question 8: Recursion - Factorial
print("\n--- Question 8: Recursion (Factorial) ---")
def factorial(n):
    """Calculate factorial of n recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(f"factorial(5) = {result}")
print(f"Expected: 120")

print(f"factorial(6) = {factorial(6)}")


# Question 9: String processing - Count vowels, consonants, digits, spaces
print("\n--- Question 9: String Processing ---")
def analyze_string(text):
    """Count vowels, consonants, digits, and spaces in a string"""
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    space_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    return vowel_count, consonant_count, digit_count, space_count

test_string = "Python 123"
vowels, consonants, digits, spaces = analyze_string(test_string)
print(f"Input: '{test_string}'")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")


# ============================================================================
# PART 3: FILE HANDLING, CSV AND JSON 
# ============================================================================

print("\n" + "=" * 70)
print("PART 3: FILE HANDLING, CSV AND JSON")
print("=" * 70)

# Question 10: Text file operations
print("\n--- Question 10: Text File Operations ---")

# Create and write to notes.txt
with open('notes.txt', 'w') as file:
    file.write("First line: Learning Python basics\n")
    file.write("Second line: Understanding data structures\n")
    file.write("Third line: Working with functions\n")
    file.write("Fourth line: File handling operations\n")
    file.write("Fifth line: Object-oriented programming\n")

print("✓ Created and wrote to notes.txt")

# Read and print complete file
print("\nReading complete file:")
with open('notes.txt', 'r') as file:
    content = file.read()
    print(content)

# Print only the third line
print("Third line only:")
with open('notes.txt', 'r') as file:
    lines = file.readlines()
    print(lines[2].strip())

# Append one more line
print("\nAppending new line to notes.txt...")
with open('notes.txt', 'a') as file:
    file.write("Sixth line: Building real-world applications\n")

print("✓ Appended successfully. Updated content:")
with open('notes.txt', 'r') as file:
    content = file.read()
    print(content)


# Question 11: CSV file operations
print("\n--- Question 11: CSV File Operations ---")
import csv

# Create employees.csv
csv_data = [
    ['id', 'name', 'salary'],
    [1, 'Alice Johnson', 50000],
    [2, 'Bob Smith', 55000],
    [3, 'Charlie Brown', 48000],
    [4, 'Diana Prince', 60000],
    [5, 'Eve Davis', 52000]
]

with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("✓ Created employees.csv with the following data:")
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# ============================================================================
# PART 4: OOP AND SINGLE INHERITANCE 
# ============================================================================

print("\n" + "=" * 70)
print("PART 4: OOP AND SINGLE INHERITANCE")
print("=" * 70)

# Question 13: Student class
print("\n--- Question 13: Student Class ---")

class Student:
    """Student class to store and display student information"""

    def __init__(self, name, roll_number, marks):
        """
        Constructor to initialize student details

        Args:
            name: Student's name
            roll_number: Student's roll number
            marks: Student's marks
        """
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        """Print all student details"""
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def check_result(self):
        """Return Pass if marks >= 40, otherwise Fail"""
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


# Create three student objects
print("Creating three student objects:\n")

student1 = Student("Priya", 101, 85)
print("Student 1:")
student1.display_details()
print(f"Result: {student1.check_result()}\n")

student2 = Student("Raj", 102, 38)
print("Student 2:")
student2.display_details()
print(f"Result: {student2.check_result()}\n")

student3 = Student("Neha", 103, 72)
print("Student 3:")
student3.display_details()
print(f"Result: {student3.check_result()}\n")


# ============================================================================
# BONUS: Enhanced OOP with Inheritance
# ============================================================================

print("\n" + "=" * 70)
print("BONUS: INHERITANCE EXAMPLE")
print("=" * 70)

class Person:
    """Base class for Person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old"


class Employee(Person):
    """Derived class Employee inheriting from Person"""
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def introduce(self):
        return f"{super().introduce()}, working in {self.department} department"


print("\nDemonstration of Inheritance:\n")
emp = Employee("Sreejaya Sreekutty", 26, "313669", "Software Testing")
print(emp.introduce())

print("\n" + "=" * 70)
print("ASSESSMENT COMPLETE!")
print("=" * 70)
