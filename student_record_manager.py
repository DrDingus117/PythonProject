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

    while True:
        try:
            age = int(input("Enter student age: "))
            break
        except ValueError:
            print("Please enter a number for age.")

    quarter = input("Enter student quarter: ")

    student = Student(student_name, student_id, grades, program, age, quarter)

    students.append(student)


# 3: Viewing Student

def view_students():
    print("\nStudent Records")

    if not students:
        print("No student records available at the moment.")
        return

    for student in students:
        print("\nName:", student.student_name)
        print("ID:", student.student_id)
        print("Grades:", student.grades)
        print("Program:", student.program)
        print("Age:", student.age)
        print("Quarter:", student.quarter)


# 4: Editing Student Records

def edit_student():
    student_id = input("Enter student ID to edit: ")

    for student in students:
        if student.student_id == student_id:
            student.student_name = input("Enter new student name: ")
            student.grades = input("Enter new student grades: ")
            student.program = input("Enter new student program: ")

            while True:
                try:
                    student.age = int(input("Enter new student age: "))
                    break
                except ValueError:
                    print("Please enter a number for age.")

            student.quarter = input("Enter new student quarter: ")

            print("Student updated")


# 5: Delete Student Records

def delete_student():
    student_id = input("Enter ID you want to remove: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student removed")
            return

    print("Student not available. Please try again.")

# 6: Saving Students

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                student.student_name + "." +
                student.student_id + "." +
                student.grades + "." +
                student.program + "." +
                str(student.age) + "." +
                student.quarter + "\n"
            )

    print("Students saved")

#7 Load Students

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(".")

                student_name = data[0]
                student_id = data[1]
                grades = data[2]
                program = data[3]
                age = int(data[4])
                quarter = data[5]

                student = Student(
                    student_name,
                    student_id,
                    grades,
                    program,
                    age,
                    quarter
                )

                students.append(student)

        print("Students loaded")

    except FileNotFoundError:
        print("No student file found. Starting with an empty list.")

# 8: Menu

def menu():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Save Students")
        print("6. Load Students")
        print("7. Exit")

        choice = input("Enter the choice you want to do: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            edit_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save_students()

        elif choice == "6":
            load_students()
      
        elif choice == "7":
            print("See Ya!")
            break

        else:
            print("Can't do that. Please try again.")


menu()