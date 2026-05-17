# Scholarsip elegibility
from studentClass import Student

class ScholarshipStudent(Student):
    @property
    def isElegible(self):
        if self.getGrade=="First":
            return "Yes"
        else:
            return "No"
    
    def display(self):
        return(self.name,self.rollnumber, self.getPer, self.getGrade)

