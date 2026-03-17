from student_manager import StudentManager

manager = StudentManager()

while True:

    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1 Add Student")
    print("2 Display Students")
    print("3 Search Student")
    print("4 Update Student")
    print("5 Delete Student")
    print("6 Sort Students")
    print("7 Export CSV")
    print("8 Generate Report")
    print("9 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = int(input("Enter roll: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        manager.add_student(roll, name, marks)

    elif choice == "2":

        manager.display_students()

    elif choice == "3":

        keyword = input("Enter roll or name: ")
        manager.search_student(keyword)

    elif choice == "4":

        roll = int(input("Enter roll to update: "))
        manager.update_student(roll)

    elif choice == "5":

        roll = int(input("Enter roll to delete: "))
        manager.delete_student(roll)

    elif choice == "6":

        manager.sort_students()

    elif choice == "7":

        manager.export_csv()

    elif choice == "8":

        manager.generate_report()

    elif choice == "9":

        print("Exiting program")
        break

    else:

        print("Invalid choice")