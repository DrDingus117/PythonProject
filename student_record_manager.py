# --------------------------------------------
# Student Record Manager Based off Java Version from Quarter 2
# --------------------------------------------

# Student class
class Student:

    # Constructor
    def __init__(self, student_id, name, age, major, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa


# List that stores every student object
students = []


# --------------------------------------------
# Add Student
# --------------------------------------------
def add_student():

    #Example of this is 117
    student_id = input("Student ID: ") #(Example: 117)

    #Example: Marcus
    name = input("Name: ") #(Example: Marcus)

    #Example: 23   
    age = int(input("Age: ")) #(Example: 23)

    #Example: Software Development
    major = input("Major: ") #(Example: Software Development)

    #Example: 3.0
    gpa = float(input("GPA: ")) #(Example: 3.0)

    student = Student(student_id, name, age, major, gpa)

    students.append(student)

    print("\nStudent added successfully.\n")


# --------------------------------------------
# View Students
# --------------------------------------------
def view_students():

    if len(students) == 0:
        print("\nNo students found.\n")
        return

    print("\n----- Student List -----")

    for student in students:
        print("------------------------")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Major:", student.major)
        print("GPA:", student.gpa)

    print()


# --------------------------------------------
# Search Student
# --------------------------------------------
def search_student():

    search_id = input("Enter Student ID: ") #(117)

    for student in students:

        if student.student_id == search_id:

            print("\nStudent Found")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Major:", student.major)
            print("GPA:", student.gpa)
            print()

            return

    print("\nStudent not found.\n")


# --------------------------------------------
# Update Student
# --------------------------------------------
def update_student():

    search_id = input("Student ID: ") #(Example: 117 can be used to update Marcus's information)

    for student in students:

        if student.student_id == search_id:

            print("Leave blank if you don't want to change a value.")

            name = input("New Name: ") #(Example: Marcus))

            if name != "":
                student.name = name

            major = input("New Major: ") #(Example: Cybersecurity)

            if major != "":
                student.major = major

            gpa = input("New GPA: ") #(Example: 3.5)

            if gpa != "":
                student.gpa = float(gpa)

            print("\nStudent updated.\n")

            return

    print("\nStudent not found.\n")


# --------------------------------------------
# Delete Student
# --------------------------------------------
def delete_student():

    search_id = input("Student ID: ") #(Example: 117 deletes Marcus from the list)

    for student in students:

        if student.student_id == search_id:

            students.remove(student)

            print("\nStudent deleted.\n")

            return

    print("\nStudent not found.\n")


# --------------------------------------------
# Save Students
# --------------------------------------------
def save_students():

    file = open("students.txt", "w") #(Example: students.txt is the file that will be created to save the students. Holds 117 for Marcus)

    for student in students:

        file.write(
            f"{student.student_id},"
            f"{student.name},"
            f"{student.age},"
            f"{student.major},"
            f"{student.gpa}\n"
        )

    file.close()

    print("\nStudents saved.\n")


# --------------------------------------------
# Load Students
# --------------------------------------------
def load_students():

    students.clear()

    try:

        file = open("students.txt", "r") #(Example: students.txt is the file that will be opened to load the students. Holds 117 for Marcus)

        for line in file:

            data = line.strip().split(",")

            student = Student(
                data[0],
                data[1],
                int(data[2]),
                data[3],
                float(data[4])
            )

            students.append(student)

        file.close()

        print("\nStudents loaded.\n")

    except FileNotFoundError:

        print("\nNo saved file found.\n")


# --------------------------------------------
# Menu
# --------------------------------------------
def menu():

    while True:

        print("===== Student Record Manager=====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Students")
        print("7. Load Students")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            save_students()

        elif choice == "7":
            load_students()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


menu()