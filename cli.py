from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent
from classRoomClass import ClassRoom
from storage.jsonStorage import StorageJSON

if __name__ == "__main__":
    class1= ClassRoom("B.Tech",[])

    class1.enroll()
    
    print("topper",class1.classTopper)

    StorageJSON.save_to_file(class1)

    class2 = ClassRoom("Loaded Class", [])
    StorageJSON.load_from_file(class2)

    print("\n--- class2 (loaded from file) ---")
    class2.show_All_Results()
    print("topper", class2.classTopper)