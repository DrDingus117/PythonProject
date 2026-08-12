# Student Record Manager based off the Java version

# 1: Student Class begining

class Student:
  def __init__(self, student_name, student_id, grades, program, age, quarter):
    self .student_name = student_name
    self .student_id = student_id
    self .grades = grades
    self .program = program
    self .age = age
    self .quarter = quarter

# 2: adding Student objects

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
