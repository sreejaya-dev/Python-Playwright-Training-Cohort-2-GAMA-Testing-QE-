"""
Question 1 - Student Marks Management System
Accepts details of multiple students, calculates their results and displays a summary.
"""

SUBJECTS = ["Python", "SQL", "AI"]
PASS_MARK = 40
TOP_PERFORMER_MARK = 75

SAMPLE_STUDENTS = [
    {"id": 101, "name": "Rahul", "marks": {"Python": 85, "SQL": 75, "AI": 80}},
    {"id": 102, "name": "Anjali", "marks": {"Python": 60, "SQL": 70, "AI": 65}},
    {"id": 103, "name": "Priya", "marks": {"Python": 78, "SQL": 74, "AI": 80}},
    {"id": 104, "name": "Arun", "marks": {"Python": 30, "SQL": 35, "AI": 40}},
]


def read_marks(subject):
    """Read marks for a subject, re-prompting until a value between 0 and 100 is entered"""
    while True:
        value = input(f"  {subject} Marks: ").strip()
        if value.isdigit() and 0 <= int(value) <= 100:
            return int(value)
        print("  Invalid marks. Please enter a number between 0 and 100.")


def accept_students():
    """Accept details of multiple students from the user"""
    students = []
    count = input("Enter number of students: ").strip()
    while not count.isdigit() or int(count) == 0:
        count = input("Please enter a valid number (1 or more): ").strip()

    for index in range(int(count)):
        print(f"\nEnter details of student {index + 1}")
        student_id = input("  Student ID: ").strip()
        name = input("  Student Name: ").strip()
        marks = {subject: read_marks(subject) for subject in SUBJECTS}
        students.append({"id": student_id, "name": name, "marks": marks})
    return students


def calculate_total(marks):
    """Return the total of all subject marks"""
    return sum(marks.values())


def calculate_average(total, subject_count):
    """Return the average marks rounded to 2 decimal places"""
    return round(total / subject_count, 2)


def calculate_grade(average):
    """Return the grade based on the average marks"""
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= PASS_MARK:
        return "D"
    else:
        return "F"


def get_result(average):
    """Return PASS if average is 40 or above, otherwise FAIL"""
    return "PASS" if average >= PASS_MARK else "FAIL"


def process_students(students):
    """Add total, average, grade and result to each student record"""
    for student in students:
        student["total"] = calculate_total(student["marks"])
        student["average"] = calculate_average(student["total"], len(SUBJECTS))
        student["grade"] = calculate_grade(student["average"])
        student["result"] = get_result(student["average"])
    return students


def find_highest_scorer(students):
    """Return the student with the highest average"""
    highest = students[0]
    for student in students:
        if student["average"] > highest["average"]:
            highest = student
    return highest


def find_top_performers(students):
    """Return names of students whose average is above 75 (list comprehension)"""
    return [student["name"] for student in students if student["average"] > TOP_PERFORMER_MARK]


def format_number(value):
    """Show whole numbers without a trailing .0 (80.0 -> 80)"""
    return int(value) if value == int(value) else value


def display_results(students):
    """Display each student's result and the overall summary"""
    print("\n===== Student Result =====")
    for student in students:
        print(f"Student ID   : {student['id']}")
        print(f"Name         : {student['name']}")
        for subject in SUBJECTS:
            print(f"{subject + ' Marks':<13}: {student['marks'][subject]}")
        print(f"Total        : {student['total']}")
        print(f"Average      : {format_number(student['average'])}")
        print(f"Grade        : {student['grade']}")
        print(f"Result       : {student['result']}")
        print("-" * 26)

    highest = find_highest_scorer(students)
    top_performers = find_top_performers(students)

    print(f"\nHighest Scoring Student: {highest['name']} "
          f"(Average: {format_number(highest['average'])})")
    print(f"Students above {TOP_PERFORMER_MARK}: "
          f"{', '.join(top_performers) if top_performers else 'None'}")


def main():
    choice = input("Use sample student data? (y/n): ").strip().lower()
    if choice == "y":
        students = [dict(student) for student in SAMPLE_STUDENTS]
    else:
        students = accept_students()

    process_students(students)
    display_results(students)


if __name__ == "__main__":
    main()
