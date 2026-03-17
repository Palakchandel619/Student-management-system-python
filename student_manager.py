import json
import csv
import logging
from student import Student

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_students()

    # ---------------- ADD STUDENT ----------------
    def add_student(self, roll, name, marks):

        try:

            for s in self.students:
                if s.roll == roll:
                    print("Roll number already exists.")
                    logging.warning("Duplicate roll attempted")
                    return

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100")
                logging.warning("Invalid marks entered")
                return

            student = Student(roll, name, marks)
            self.students.append(student)

            self.save_students()

            logging.info(f"Student added: {name}")
            print("Student added successfully")

        except Exception as e:
            logging.error(f"Error adding student: {e}")
            print("Error occurred while adding student")

    # ---------------- DISPLAY ----------------
    def display_students(self):

        if not self.students:
            print("No students available")
            return

        for s in self.students:
            print(s)

    # ---------------- SEARCH ----------------
    def search_student(self, keyword):

        found = False

        for s in self.students:

            if str(s.roll) == str(keyword) or s.name.lower() == keyword.lower():
                print(s)
                found = True

        if not found:
            print("Student not found")

    # ---------------- UPDATE ----------------
    def update_student(self, roll):

        try:

            for s in self.students:

                if s.roll == roll:

                    name = input("Enter new name: ")
                    marks = int(input("Enter new marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100")
                        return

                    s.name = name
                    s.marks = marks

                    self.save_students()

                    logging.info(f"Student updated: {roll}")
                    print("Student updated successfully")
                    return

            print("Student not found")

        except Exception as e:
            logging.error(f"Update error: {e}")
            print("Error updating student")

    # ---------------- DELETE ----------------
    def delete_student(self, roll):

        try:

            for s in self.students:

                if s.roll == roll:
                    self.students.remove(s)

                    self.save_students()

                    logging.info(f"Student deleted: {roll}")
                    print("Student deleted successfully")
                    return

            print("Student not found")

        except Exception as e:
            logging.error(f"Delete error: {e}")
            print("Error deleting student")

    # ---------------- SORT ----------------
    def sort_students(self):

        self.students.sort(key=lambda x: x.marks, reverse=True)

        print("\nStudents sorted by marks:\n")

        for s in self.students:
            print(s)

    # ---------------- CSV EXPORT ----------------
    def export_csv(self):

        try:

            with open("students.csv", "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(["Roll", "Name", "Marks"])

                for s in self.students:
                    writer.writerow([s.roll, s.name, s.marks])

            logging.info("CSV export successful")
            print("Students exported to CSV file")

        except Exception as e:
            logging.error(f"CSV export error: {e}")
            print("Error exporting CSV")

    # ---------------- REPORT GENERATION ----------------
    def generate_report(self):

        try:

            if not self.students:
                print("No data available")
                return

            total = 0
            highest = max(self.students, key=lambda x: x.marks)
            lowest = min(self.students, key=lambda x: x.marks)

            for s in self.students:
                total += s.marks

            avg = total / len(self.students)

            with open("report.txt", "w") as file:

                file.write("STUDENT REPORT\n")
                file.write("====================\n\n")

                file.write(f"Total Students: {len(self.students)}\n")
                file.write(f"Average Marks: {avg:.2f}\n")

                file.write(f"\nTopper: {highest.name} ({highest.marks})\n")
                file.write(f"Lowest: {lowest.name} ({lowest.marks})\n")

            logging.info("Report generated")
            print("Report generated successfully")

        except Exception as e:
            logging.error(f"Report generation error: {e}")
            print("Error generating report")

    # ---------------- LOAD JSON ----------------
    def load_students(self):

        try:

            with open("students.json", "r") as file:

                data = json.load(file)

                for item in data:
                    student = Student.from_dict(item)
                    self.students.append(student)

        except FileNotFoundError:
            logging.info("JSON file not found. Starting fresh.")

    # ---------------- SAVE JSON ----------------
    def save_students(self):

        try:

            data = []

            for s in self.students:
                data.append(s.to_dict())

            with open("students.json", "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            logging.error(f"Save error: {e}")