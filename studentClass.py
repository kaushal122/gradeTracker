
class Student:
    def __init__(self,name, rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        self.__marks=[]
    
    def addMarks(self, mark):
        if mark>0 and mark<=100:
            self.__marks.append(mark)
            return 1
        else:
            print(f"Invalide mark: {mark}")
            return 0
    
    def getMarks(self):
        return list(self.__marks)
    @property
    def getAvg(self):
        sum=0
        for mark in self.__marks:
            sum+=mark
        return sum//(len(self.__marks))
    @property
    def getPer(self):
        sm=sum(self.__marks)
        sub=len(self.__marks)*100
        return (sm*100)//sub
    @property
    def getGrade(self):
        if self.getPer>60:
            return "First"
        elif self.getPer>50:
            return "Second"
        else:
            return "Better Luck Next Time"
        
    def display(self):
        return(self.name, self.rollnumber, self.getPer, self.getGrade)






        