#ClassRoom
from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent
from storage.sqlite_storage import get_MaxRollNumber, save_student
import os


class ClassRoom:
    def __init__(self,name, students:list):
        self.name=name
        self.__students=students

    def enroll(self,db_path: str, classroom_id: int):
        count=int(input(f"How many students to enroll: "))
        if count==0:
            return
        for _ in range(count):
            name=input("Enter student name:")
            rollnumber=get_MaxRollNumber(db_path,classroom_id)+1
            student1=Student(name,rollnumber)
            for i in range(3):
                mark=int(input(f"Enter mark of the subject {i+1} : "))
                while not student1.addMarks(mark):
                    mark=int(input(f"Enter mark of the subject {i+1} : "))
            save_student(db_path, student1, classroom_id)
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

    @property
    def students(self):
        return self.__students
    
    @students.setter
    def students(self, students):
        self.__students = students


