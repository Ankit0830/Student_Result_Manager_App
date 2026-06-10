# import cursor from database
from db_connection import conn, cursor

while True:
    print("\n----- STUDENT MANAGER APP -----\n")
    print("1. Add Students")
    print("2. Add Subject Marks")
    print("3. Delete Students")
    print("4. View Students")
    print("5. Students Grade")
    print("6. Update Marks")
    print("7. Students Percentage")
    print("8. Check Result")
    print("9. Show Topper")
    print("10. Exit")

    # Add student
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        
        query = """
        INSERT INTO students(name)
        VALUES(%s)
        """

        cursor.execute(query, (name,))
        conn.commit()

        print("Student Added Successfully!")

    # add subject and marks
    elif choice == "2":
        student_id = int(input("Enter Student ID: "))
        subject = input("Enter Subject Name: ")
        marks = int(input("Enter Marks: "))

        query = """
        INSERT INTO marks
        (student_id, subject_name, marks)
        VALUES(%s, %s, %s)
        """

        cursor.execute(
            query,
            (student_id, subject, marks)
        )

        conn.commit()

        print("Subject Marks Added Successfully!")

    # Delete student 
    elif choice == "3":
        student_id = int(input("Enter Student ID: "))

        query = """
        DELETE FROM students
        WHERE id = %s
        """

        cursor.execute(query, (student_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully!")
        else:
            print("Student ID not found!")
        # if name in students:
        #     students.pop(name)
        #     print(f"{name} Successfully deleted!")
        # else:
        #     print("Student not found!")

    # View student
    elif choice == "4":
        query = """
        SELECT s.id,
            s.name,
            m.subject_name,
            m.marks
        FROM students s
        JOIN marks m
        ON s.id = m.student_id
        ORDER BY s.id
        """

        cursor.execute(query)
        records = cursor.fetchall()

        if records:
            print("\nID\tName\tMarks")
            print("-" * 25)

            for row in records:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
        else:
            print("No students found!")

        # if not student:
        #     print("No student found!")

        # else:
        #     for name, marks in student.items():
        #         print(name, ":", marks)

    # Grade of student
    elif choice == "5":
        student_id = int(input("Enter Student ID: "))

        # query = "SELECT marks FROM students WHERE id = %s"
        query = """
        SELECT AVG(marks)
        FROM marks
        WHERE student_id = %s"""

        cursor.execute(query, (student_id,))
        result = cursor.fetchone()

        if result:
            percentage = result[0]

            if percentage >= 95:
                print("A+ Grade")
            elif percentage >= 75:
                print("A Grade")
            elif percentage >= 50:
                print("B Grade")
            elif percentage >= 25:
                print("C Grade")
            else:
                print("FAIL")
        else:
            print("Student not found!")

    # elif choice == "4":
    #     name = input("Enter student name: ")

    #     if name in students:
    #         marks = students[name]

    #         if marks >= 95:
    #             print("A+ Grade")

    #         elif marks <= 95 and marks >= 75:
    #             print("A Grade")

    #         elif marks <= 75 and marks >= 50:
    #             print("B Grade")

    #         elif marks <= 50 and marks >= 25:
    #             print("C Grade")

    #         else:
    #             print("FAIL!")

    #     else:
    #         print("Students not found!")

    # Update marks
    elif choice == "6":
        student_id = int(input("Enter Student ID: "))
        new_marks = int(input("Enter New Marks: "))

        if 0 <= new_marks <= 100:

            query = """
            UPDATE students
            SET marks = %s
            WHERE id = %s
            """

            cursor.execute(query, (new_marks, student_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("Marks Updated Successfully!")
            else:
                print("Student ID not found!")

        else:
            print("Marks must be between 0 and 100")

            # if name in students:
            #     new_marks = int(input("Enter new marks: "))
            #     students[name] = new_marks
            #     # student.update([name: new_marks])
            #     print("Marks updated successfully!")
            # else:
            #     print("Students not found!")

    # Students percentage
    elif choice == "7":
        student_id = int(input("Enter Student ID: "))

        query = """
        SELECT AVG(marks)
        FROM marks
        WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))

        result = cursor.fetchone()

        if result and result[0]:
            print(f"Percentage: {result[0]:.2f}%")
        else:
            print("No marks found!")


    # elif choice == "6":
    #     name = input("Enter student name: ")

    #     if name in students:
    #         marks = students[name]
    #         percentage = (marks / 100) * 100
    #         print(f"Percentage: {percentage}%")
    #     else:
    #         print("Students not found!")


    # Check result
    elif choice == "8":
        student_id = int(input("Enter Student ID: "))

        query = """
        SELECT AVG(marks)
        FROM marks
        WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))
        result = cursor.fetchone()

        if result:
            average = result[0]

            if average >= 40:
                print("PASS!")
            else:
                print("FAIL!")
        else:
            print("Student not found!")



        # name = input("Enter students name:")

        # if name in students:
        #     marks = students[name]

        #     if marks >= 40:
        #         print("PASS! ")
        #     else:
        #         print("FAIL!")
        # else:
        #     print("Students Not Found! ")

    # Show Topper
    elif choice == "9":
        query = """
        SELECT s.id,
            s.name,
            AVG(m.marks) AS percentage
        FROM students s
        JOIN marks m
        ON s.id = m.student_id
        GROUP BY s.id, s.name
        ORDER BY percentage DESC
        LIMIT 1
        """

        cursor.execute(query)
        topper = cursor.fetchone()

        if topper:
            print("\nTopper Details")
            print(f"ID: {topper[0]}")
            print(f"Name: {topper[1]}")
            print(f"Marks: {topper[2]}")
        else:
            print("No students found!")

    # elif choice == "8":
    #     if students:
    #         topper = max(students, key=student.get)
    #         print(f"Topper:{topper} \n Marks: {students[topper]}")

    #     else:
    #         print("No student found!")
    
    # Exit
    elif choice == "10":
        print("Exiting.........")
        break

    else:
        print("In-valid Input! ")