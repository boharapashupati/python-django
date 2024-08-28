#write a program to make crud application for school.
# School CRUD Applicatio.
# Initialize an empty dictionary to store student data
students = {}

def create_student():
    name = input("Enter student name: ")
    roll_no = input("Enter student roll number: ")
    grade = input("Enter student grade: ")
    students[roll_no] = {"name": name, "grade": grade}
    print("Student created successfully!")

def read_student():
    roll_no = input("Enter student roll number: ")
    if roll_no in students:
        print("Student Name:", students[roll_no]["name"])
        print("Student Grade:", students[roll_no]["grade"])
    else:
        print("Student not found!")

def update_student():
    roll_no = input("Enter student roll number: ")
    if roll_no in students:
        name = input("Enter new student name: ")
        grade = input("Enter new student grade: ")
        students[roll_no]["name"] = name
        students[roll_no]["grade"] = grade
        print("Student updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll_no = input("Enter student roll number: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def display_all_students():
    for roll_no, student in students.items():
        print("Roll No:", roll_no)
        print("Student Name:", student["name"])
        print("Student Grade:", student["grade"])
        print("---------")

while True:
    print("School CRUD Application")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        read_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_all_students()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again!")

