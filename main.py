# main.py

from student import add_student, view_students, delete_student
from course import add_course, view_courses
from enrollment import enroll_student, view_enrollments
from datetime import datetime,date

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Enroll Student")
        print("7. View Enrollments")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            reg_no = input("Regn_no: ")
            gender = input("gender: ")
            address = input("address: ")
            Mob = input("Mobile No: ")
            DOB = datetime.strptime(input("DOB (YYYY-MM-DD): "), "%Y-%m-%d").date()
            add_student(name,reg_no,DOB,gender,address,Mob)

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_id = int(input("reg_no to delete: "))
            delete_student(reg_no)

        elif choice == "4":
            name = input("Course Name: ")
            course_id = int(input("course_id: "))
            add_course(name, course_id)

        elif choice == "5":
            view_courses()

        elif choice == "6":
            reg_no = input("Reg_NO: ")
            course_id = int(input("Course ID: "))
            enrollment_date=date.today()
            enroll_student(student_id, course_id,enrollment_date)

        elif choice == "7":
            view_enrollments()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
