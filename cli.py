from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent
from classRoomClass import ClassRoom
from storage.sqlite_storage import init_db, load_all_students, delete_student, update_marks, save_classroom
import requests
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    path=os.getenv("dbPath")
    init_db(path)
    classroom=input("Enter Class name: ")
    classroom_id=save_classroom(path,classroom)
    existing = load_all_students(path,classroom_id)
    class1= ClassRoom(classroom, existing)
    while True:
        print("\n---Menu---")
        print("1. Enroll Students")
        print("2. Show all results")
        print("3. Show topper")
        print("4. Load from DB")
        print("5. Delete a Student")
        print("6. Update Marks")
        print("7. Exit")

        choice = input("Enter the Choice:")

        if choice=="1":
            class1.enroll(path, classroom_id)

        elif choice=="2":
            class1.show_All_Results()

        elif choice=="3":
            print(class1.classTopper)

        elif choice=="4":
            class1.students = load_all_students(path, classroom_id)
            class1.show_All_Results()

        elif choice=="5":
            rL=int(input("Provide Rollnumber: "))
            delete_student(path,rL)
            class1.students = [s for s in class1.students if s.rollnumber != rL]

        elif choice == "6":
            rn = int(input("Enter rollnumber: "))
            marks = []
            for i in range(3):
                temp = int(input(f"Enter subject {i+1} marks: "))
                marks.append(temp)
            update_marks(path, rn, marks)

        elif choice=="7":
            break

    url="https://official-joke-api.appspot.com/random_joke"
    joke=requests.get(url).json()
    print("Joke for Toppper:----> ",joke["setup"])
