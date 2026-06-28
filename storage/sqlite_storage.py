import sqlite3
from models.studentClass import Student
def init_db(db_path:str) ->None:
    #connect to database
    conn=sqlite3.connect(db_path)

    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classrooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rollNumber INTEGER,
            marks TEXT,
            classroom_id INTEGER,
            FOREIGN KEY (classroom_id) REFERENCES classrooms(id)
            UNIQUE (rollnumber, classroom_id)
                )
    """
    )
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_Analysis(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   classroom_id INTEGER,
                   top_performer TEXT,
                   needs_help TEXT,
                   class_Average REAL,
                   olympiad_candidate TEXT,
                   summary TEXT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (classroom_id) REFERENCES classrooms(id)
                   )
                """
                )

    conn.commit()
    conn.close()

#init_db("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db")

def save_classroom(db_path:str,classroom_name:str)->int:
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute(
        " INSERT OR IGNORE INTO classrooms (name) VALUES(?)",
        (classroom_name,)
    )
    conn.commit()
    cursor.execute(
        " SELECT id FROM classrooms WHERE name=?",
        (classroom_name,)
    )
    classroom_id=cursor.fetchone()[0]
    conn.close()
    return classroom_id

def save_student(db_path:str,student:Student, classroom_id:int) ->None:

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    marks_str = ",".join(str(m) for m in student.getMarks())
    cursor.execute("INSERT OR IGNORE INTO students(name,rollnumber,marks, classroom_id) VALUES (?,?,?,?)",
                   (student.name, student.rollnumber,marks_str,classroom_id)
                   )
    conn.commit()
    conn.close()


def load_all_students(db_path:str, classroom_id:int)->list:

    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute(
        """
            SELECT name, rollnumber, marks FROM students WHERE classroom_id=?
        """,
        (classroom_id,)
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

#data=load_all_students("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db")
#for st in data:
#    print(st.name,st.rollnumber)


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

#delete_student("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db",6)

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
#marksup=[78,89,90]
#update_marks("/Users/radhe/Projects/WebDevPython/OOps1/GradingSystem/storage/classRoom.db",1,marksup)

def get_MaxRollNumber(db_path:str,classroom_id:int)->int:
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    cursor.execute(" SELECT MAX(rollnumber) FROM students WHERE classroom_id=?",
                   (classroom_id,))
    result=cursor.fetchone()[0]
    conn.close()
    return result if result is not None else 0


def save_analysis(dbpath:str, classroom_id:int,parsed:dict)-> None:
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    
    cursor.execute(
        """  INSERT INTO ai_Analysis(classroom_id, top_performer, need_help, class_Average, olympiad_candidate, summary) 
        Values(?,?,?,?,?,?)
          
    """,(classroom_id,parsed["top_performer"]["name"],parsed["needs_help"]["name"],parsed["class_average"], parsed["olympiad_candidate"],parsed["overall_summary"])
    )

    conn.commit()
    conn.close()

    return

def get_all_students_tool(db_path:str, classroom_id:int) -> list:
    students = load_all_students(db_path, classroom_id)
    return [
        {
            "name":st.name, "rollnumber": st.rollnumber,
            "percentage":st.getPer, "grade": st.getGrade
        }
        for st in students
    ]

def get_topper_tool(db_path:str, classroom_id:int)-> dict:
    students= load_all_students(db_path, classroom_id)
    if not students:
        return {"error" : "No student found"}
    topper=max(students,key=lambda st:st.getPer)
    return {"name": topper.name, "percentage":topper.getPer}

def get_class_average_tool(db_path: str, classroom_id: int) -> dict:
    students = load_all_students(db_path, classroom_id)
    if not students:
        return {"error": "No students found"}
    avg = sum(st.getPer for st in students) / len(students)
    return {"class_average": round(avg, 2)}