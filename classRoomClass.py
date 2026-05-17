#ClassRoom
from studentClass import Student
from ScholarshipStudentClass import ScholarshipStudent

class ClassRoom:

    def __init__(self,name, students:list):
        self.name=name
        self.__students=students
    
    def enroll(self):
        st=int(input(f"How many students to enroll: "))
        if st==0:
            return
        for _ in range(st):
            name=input("Enter student name:")
            marks=[]
            st1=Student(name,len(self.__students)+1)
            for i in range(3):
                mark=int(input(f"Enter mark of the subject {i+1} : "))
                while not st1.addMarks(mark):
                    mark=int(input(f"Enter mark of the subject {i+1} : "))
            self.__students.append(st1)
        
        
    
    def show_All_Results(self):
        for st in self.__students:
            print(st.display())
    
    @property
    def classTopper(self):
        maxPer=0
        topper=""
        for st in self.__students:
            if st.getPer > maxPer:
                maxPer=st.getPer
                topper=st.name
        
        return topper


c1= ClassRoom("B.Tech",[])

c1.enroll()

c1.show_All_Results() 
print(c1.classTopper)