from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent
from classRoomClass import ClassRoom
import json
class StorageJSON:
    @staticmethod
    def save_to_file(classRoom,fileName="classRoom.json"):
        data={
            "classroom": classRoom.name,
            "students":[
                {
                    "name":student.name,
                    "rollnumber":student.rollnumber,
                    "marks":student.getMarks()
                    
                }
                for student in classRoom.getStudents()
            ]
        }
        with open (fileName, "w") as f:
            json.dump(data,f, indent=4)
        print(f"Saved to file {fileName}")


    def load_from_file(classRoom, fileName="classRoom.json"):
        try:
            with open(fileName,"r") as f:
                data=json.load(f)
            students=[]
            
            for student in data["students"]:
                newStudent=Student(student["name"], student["rollnumber"])
                for mark in student["marks"]:
                    newStudent.addMarks(mark)
                students.append(newStudent)
            
            classRoom.setStudents(students)

            print(f"Loaded {len(students)} students from {fileName}")
        except FileNotFoundError:
            print(f"No file found: {fileName}")
        except json.JSONDecodeError:
            print("File is corrupted or not valid JSON")