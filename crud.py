def add_student(connection):
        cursor = connection.cursor()
        name = input("Enter student's name: ")
        try:
            age = int(input("Enter student's age: "))
        except ValueError:
            print("Enter a valid age.")
            return
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
             print("Enter a valid GPA.")
             return
        cursor.execute("""
        INSERT INTO students 
        (name, age, gpa)

        VALUES (?, ?, ?)
        """, (name, age, gpa))

        connection.commit()

def show_students(connection):
        cursor = connection.cursor()
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

def update_gpa(connection):
        cursor = connection.cursor()
        student_id = int(input("Enter student ID: "))
        try:
            new_gpa = float(input("Enter new GPA: "))
        except ValueError:
             print("Enter a valid GPA.")
             return
        cursor.execute("""
        UPDATE students

        SET gpa = ?

        WHERE id = ?
        """, (new_gpa, student_id))

        connection.commit()

def delete_student(connection):
        cursor = connection.cursor()
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
             print("Enter a valid student ID.")
             return
        cursor.execute("""
        DELETE FROM students

        WHERE id = ?
        """, (student_id,))

        connection.commit()