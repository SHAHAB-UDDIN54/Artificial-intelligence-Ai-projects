students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\nAll Students:")
    print("Roll\tName\tMarks")
    for roll, info in students.items():
        print(f"{roll}\t{info['name']}\t{info['marks']}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        student = students[roll]
        print("Student Found:")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")

def update_marks():
    roll = input("Enter Roll Number to update marks: ")
    if roll in students:
        new_marks = input("Enter new marks: ")
        students[roll]["marks"] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main Menu Loop
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")
