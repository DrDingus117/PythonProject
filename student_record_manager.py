# Student Record Manager based off the Java version

# 1: Student Class beginning

class Student:
    def __init__(self, student_name, student_id, grades, program, age, quarter):
        self.student_name = student_name
        self.student_id = student_id
        self.grades = grades
        self.program = program
        self.age = age
        self.quarter = quarter


# 2: Adding Student objects

students = []


def add_student():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grades = input("Enter student grades (comma-separated): ")
    program = input("Enter student program: ")
    age = int(input("Enter student age: "))
    quarter = input("Enter student quarter: ")

    student = Student(student_name, student_id, grades, program, age, quarter)

    students.append(student)


# 3: Menu

def menu():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. Exit")

        choice = input("Enter the choice you want to do: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            print("See Ya!")
            break

        else:
            print("Can't do that. Please try again.")


menu()