import sqlite3
from models.studentClass import Student
def init_db(db_path:str) ->None:
    #connect to database
    conn=sqlite3.connect(db_path)

    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rollNumber INTEGER UNIQUE,
            marks TEXT
                )
    """
    )

    conn.commit()
    conn.close()

init_db("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db")

def save_student(db_path:str,student:Student) ->None:

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute("INSERT INTO students(name,rollnumber,marks) VALUES (?,?,?)",
                   (student.name, student.rollnumber, ",".join(str(m) for m in student.getMarks()))
                   )
    conn.commit()
    conn.close()

s=Student("Rinla9",14)
s.addMarks(85)
s.addMarks(90)
s.addMarks(99)

save_student("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db",s)

def load_all_students(db_path:str)->list:

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute(
        """
            SELECT name, rollnumber, marks FROM students
        """
    )
    
    rows=cursor.fetchall()
    data=[]
    for elem in rows:
        name=elem[0]
        rollnumb=elem[1]
        marks=[int(m) for m in elem[2].split(",")]
        temp=Student(name,rollnumb)
        for mark in marks:
            temp.addMarks(mark)
        data.append(temp)
       
   # print(rows)
    
    conn.commit()
    conn.close()
    return data

data=load_all_students("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db")
for st in data:
    print(st.name,st.rollnumber)


def delete_student(db_path:str,rollnumber:int)->None:
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
        
    cursor.execute(
        """
            DELETE FROM students WHERE rollnumber=?
        """,
        (rollnumber,)
    )


    conn.commit()
    conn.close()

delete_student("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db",6)

def update_marks(db_path:str, rollnumber:int, marks:list)->None:
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute(
        """
           UPDATE students SET marks=?   WHERE rollnumber=?

        """, (",".join(str(m) for m in marks),rollnumber)


    )
    conn.commit()
    conn.close()
marksup=[78,89,90]
update_marks("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db",1,marksup)