Student Management System
Project Overview

The Student Management System is a Python-based console application that allows users to manage student records efficiently.
It uses Object-Oriented Programming (OOP) concepts and stores student data in a JSON file for persistence.

This project demonstrates industry-style features such as data validation, logging, error handling, CSV export, and report generation.
Features
Basic Features

Add new student records

Display all students

Search student by roll number or name

Update student details

Delete student records

Level 2 Improvements

Duplicate roll number prevention

Marks validation (0–100)

__str__() method for clean display

Better search functionality

Automatic sorting of students

Level 3 (Industry Style Features)

Logging system (system.log)

Error handling using try/except

CSV export (students.csv)

Report generation (total students, average marks, topper)

Technologies Used

Python

JSON (for data storage)

CSV module

Logging module

Project Structure
Student_Management_System
│
├── main.py              # Main menu-driven program
├── student.py           # Student class
├── student_manager.py   # Business logic and operations
│
├── students.json        # Database file
├── students.csv         # Exported data file
├── system.log           # Logging file
│
└── README.md
How the System Works

The program starts from main.py.

A StudentManager object is created.

Existing student data is loaded from students.json.

The user interacts through a menu-driven interface.

Any change in data is automatically saved to the JSON file.

Additional files such as CSV export and logs are generated when required.

How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/yourusername/student-management-system.git
Step 2: Navigate to Project Folder
cd student-management-system
Step 3: Run the Program
python main.py
Example Menu
Student Management System
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Export to CSV
7. Generate Report
8. Exit
Example Output

Add Student:

Enter roll number: 1
Enter name: Rahul
Enter marks: 85
Student added successfully.

Search Student:

Enter roll number or name to search: Rahul
Roll: 1, Name: Rahul, Marks: 85

Report Generation:

--- Student Report ---
Total Students: 5
Average Marks: 78.4
Topper: Priya (92)
Files Generated Automatically
File	Purpose
students.json	Stores student records
students.csv	Exported student data
system.log	Logs system activities
Concepts Used

Object-Oriented Programming (OOP)

File Handling

JSON Data Storage

Error Handling

Logging System

Data Validation

CSV File Handling

Future Improvements

Possible upgrades for future versions:

Graphical User Interface (GUI) using Tkinter

Database integration using SQLite

Student performance graphs

Login authentication system

Web-based version using Flask or Django

Author

Palak Chandel
BCA AIML Student
