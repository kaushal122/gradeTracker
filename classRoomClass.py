#ClassRoom
from studentClass import Student
from ScholarshipStudentClass import ScholarshipStudent
import json

class ClassRoom:

    def __init__(self,name, students:list):
        self.name=name
        self.__students=students
    
    def enroll(self):
        student=int(input(f"How many students to enroll: "))
        if student==0:
            return
        for _ in range(student):
            name=input("Enter student name:")
            marks=[]
            student1=Student(name,len(self.__students)+1)
            for i in range(3):
                mark=int(input(f"Enter mark of the subject {i+1} : "))
                while not student1.addMarks(mark):
                    mark=int(input(f"Enter mark of the subject {i+1} : "))
            self.__students.append(student1)
        
        
    
    def show_All_Results(self):
        for student in self.__students:
            print(student.display())
    
    @property
    def classTopper(self):
        maxPer=0
        topper=""
        for student in self.__students:
            if student.getPer > maxPer:
                maxPer=student.getPer
                topper=student.name
        if topper=="":
            return "None is topper currently"
        else:
            return topper

    def save_to_file(self,fileName="classRoom.json"):
        data={
            "classroom": self.name,
            "students":[
                {
                    "name":student.name,
                    "rollnumber":student.rollnumber,
                    "marks":student.getMarks()
                    
                }
                for student in self.__students
            ]
        }
        with open (fileName, "w") as f:
            json.dump(data,f, indent=4)
        print(f"Saved to file {fileName}")


    def load_from_file(self, fileName="classRoom.json"):
        try:
            with open(fileName,"r") as f:
                data=json.load(f)
            self.__students=[]
            
            for student in data["students"]:
                newStudent=Student(student["name"], student["rollnumber"])
                for mark in student["marks"]:
                    newStudent.addMarks(mark)
                self.__students.append(newStudent)
            print(f"Loaded {len(self.__students)} students from {fileName}")
        except FileNotFoundError:
            print(f"No file found: {fileName}")
        except json.JSONDecodeError:
            print("File is corrupted or not valid JSON")



if __name__ == "__main__":
    class1= ClassRoom("B.Tech",[])

    class1.enroll()
    
    print("topper",class1.classTopper)

    class1.save_to_file()

    class2 = ClassRoom("Loaded Class", [])
    class2.load_from_file()

    print("\n--- class2 (loaded from file) ---")
    class2.show_All_Results()
    print("topper", class2.classTopper)
