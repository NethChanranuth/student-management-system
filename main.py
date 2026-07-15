import sqlite3

def add_student():
        name = input("Enter student's name: ")
        try:
            age = int(input("Enter student's age: "))
        except:
            print("Enter a valid age.")
        try:
            gpa = float(input("Enter student's GPA: "))
        except:
             print("Enter a valid GPA.")
        cursor.execute("""
        INSERT INTO students 
        (name, age, gpa)

        VALUES (?, ?, ?)
        """, (name, age, gpa))

        connection.commit()

def show_students():
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

def update_gpa():
        student_id = int(input("Enter student ID: "))
        try:
            new_gpa = float(input("Enter new GPA: "))
        except:
             print("Enter a valid GPA.")
        cursor.execute("""
        UPDATE students

        SET gpa = ?

        WHERE id = ?
        """, (new_gpa, student_id))

        connection.commit()

def delete_student():
        try:
            student_id = int(input("Enter student ID: "))
        except:
             print("Enter a valid student ID.")
        cursor.execute("""
        DELETE FROM students

        WHERE id = ?
        """, (student_id,))

        connection.commit()

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
        add_student()
    
    elif choice == "2": 
        show_students()
    
    elif choice == "3":
        update_gpa()
    
    elif choice == "4":
        delete_student()

    elif choice == "5":
        connection.close()
        exit = 1
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()