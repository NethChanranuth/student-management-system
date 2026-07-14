import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gpa REAL
);
""")

exit = 0

while exit==0:
    print("------Student Management System------")
    print("1. Add Student")
    print("2. Show all students")
    print("3. Update Student's GPA")
    print("4. Delete Student")
    print("5. Exit Application")

    choice = input("User Choice: ")

    if choice == "1":

        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        gpa = float(input("Enter student's GPA: "))
        cursor.execute("""
        INSERT INTO students 
        (name, age, gpa)

        VALUES (?, ?, ?)
        """, (name, age, gpa))

        connection.commit()
    
    elif choice == "2": 
        cursor.execute("""
        SELECT * FROM students
        """)
        read = cursor.fetchall()

        for student in read:
            print("--------------------")

            print(f"ID: {student[0]}")

            print(f"Name: {student[1]}")

            print(f"Age: {student[2]}")

            print(f"GPA: {student[3]}")
    
    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        new_gpa = float(input("Enter new GPA: "))
        cursor.execute("""
        UPDATE students

        SET gpa = ?

        WHERE id = ?
        """, (new_gpa, student_id))

        connection.commit()
    
    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        cursor.execute("""
        DELETE FROM students

        WHERE id = ?
        """, (student_id,))

        connection.commit()

    elif choice == "5":
        connection.close()
        exit = 1
    
    else:
        print("Invalid choice.")
