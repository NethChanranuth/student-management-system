from database import *
from crud import *

def main():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gpa REAL
    );
    """)

    running = True

    while running:
        print("------Student Management System------")
        print("1. Add Student")
        print("2. Show all students")
        print("3. Update Student's GPA")
        print("4. Delete Student")
        print("5. Exit Application")

        choice = input("User Choice: ")

        if choice == "1":
            add_student(connection)
        
        elif choice == "2": 
            show_students(connection)
        
        elif choice == "3":
            update_gpa(connection)
        
        elif choice == "4":
            delete_student(connection)

        elif choice == "5":
            connection.close()
            running = False
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()