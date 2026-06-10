student = {}

while True:
    print("\n----- STUDENT MANAGER APP -----\n")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. View Student")
    print("4. Student Grade")
    print("5. Update Marks")
    print("6. Student Percentage")
    print("7. Check Result")
    print("8. Show Topper")
    print("9. Exit")

    # Add student
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")

    # Delete student 
    elif choice == "2":
        name = input("Enter name of student:")
        if name in student:
            student.pop(name)
            print(f"{name} Successfully deleted!")
        else:
            print("Student not found!")

    # View student
    elif choice == "3":
        if not student:
            print("No student found!")

        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Grade of student
    elif choice == "4":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 95:
                print("A+ Grade")

            elif marks <= 95 and marks >= 75:
                print("A Grade")

            elif marks <= 75 and marks >= 50:
                print("B Grade")

            elif marks <= 50 and marks >= 25:
                print("C Grade")

            else:
                print("FAIL!")

        else:
            print("Student not found!")

    # Update marks
    elif choice == "5":
        name = input("Enter student name:")

        if name in student:
            new_marks = int(input("Enter new marks: "))
            student[name] = new_marks
            # student.update([name: new_marks])
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # Student percentage
    elif choice == "6":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]
            percentage = (marks / 100) * 100
            print(f"Percentage: {percentage}%")
        else:
            print("Student not found!")


    # Check result
    elif choice == "7":
        name = input("Enter student name:")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("PASS! ")
            else:
                print("FAIL!")
        else:
            print("Student Not Found! ")

    # Show Topper
    elif choice == "8":
        if student:
            topper = max(student, key=student.get)
            print(f"Topper:{topper} \n Marks: {student[topper]}")

        else:
            print("No student found!")
    
    # Exit
    elif choice == "9":
        print("Exiting.........")
        break

    else:
        print("In-valid Input! ")