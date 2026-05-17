#ClassRoom
from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent


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

    @property
    def students(self):
        return self.__students
    
    @students.setter
    def students(self, students):
        self.__students = students


