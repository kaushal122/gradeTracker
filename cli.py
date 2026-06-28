from models.studentClass import Student
from models.ScholarshipStudentClass import ScholarshipStudent
from classRoomClass import ClassRoom
from storage.sqlite_storage import init_db, load_all_students, delete_student, update_marks, save_classroom, save_analysis, get_all_students_tool, get_class_average_tool, get_topper_tool
import requests
from dotenv import load_dotenv
import os
import anthropic
import json
from tools import tools


if __name__ == "__main__":
    load_dotenv()
    client=anthropic.Anthropic()
    path=os.getenv("dbPath")
    init_db(path)
    classroom=input("Enter Class name: ")
    classroom_id=save_classroom(path,classroom)
    existing = load_all_students(path,classroom_id)
    class1= ClassRoom(classroom, existing)
    while True:
        print("\n---Menu---")
        print("1. Enroll Students")
        print("2. Show all results")
        print("3. Show topper")
        print("4. Load from DB")
        print("5. Delete a Student")
        print("6. Update Marks")
        print("7 Call Anthropic")
        print("8 chat with AI")
        print("9: Get JSON Analysis")
        print("10: Ask any question to claude about class")
        print("11. Exit")

        choice = input("Enter the Choice:")

        if choice=="1":
            class1.enroll(path, classroom_id)

        elif choice=="2":
            class1.show_All_Results()

        elif choice=="3":
            print(class1.classTopper)

        elif choice=="4":
            class1.students = load_all_students(path, classroom_id)
            class1.show_All_Results()

        elif choice=="5":
            rL=int(input("Provide Rollnumber: "))
            delete_student(path,rL)
            class1.students = [s for s in class1.students if s.rollnumber != rL]

        elif choice == "6":
            rn = int(input("Enter rollnumber: "))
            marks = []
            for i in range(3):
                temp = int(input(f"Enter subject {i+1} marks: "))
                marks.append(temp)
            update_marks(path, rn, marks)

        elif choice=="7":
            class1.students = load_all_students(path, classroom_id)
            summary=f"Class: {class1.name}\n"
            summary+=f"Total Students: {len(class1.students)} \n"
            summary+=f"Students: \n"
            for st in class1.students:
                summary += f"- {st.name} | {st.getPer} | {st.getGrade} \n"

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system="You are an academic performance analyst. When given student data, provide concise insights, identify at-risk students, and suggest specific improvement actions.",
                messages=[
                    {
                        "role": "user",
                        "content": summary
                    }
                ]
            )
            print(response.content[0].text)

        elif choice=="8":
            class1.students = load_all_students(path, classroom_id)
            summary=f"Class: {class1.name}\n"
            summary+=f"Total Students: {len(class1.students)} \n"
            summary+=f"Students: \n"
            for st in class1.students:
                summary += f"- {st.name} | {st.getPer} | {st.getGrade} \n"
            
            msg_history=[
                {"role":"user", "content": summary}
            ]

            response = client.messages.create(
                model="claude-sonnet-4-6",
                temperature=0.4,
                max_tokens=1024,
                system="You are an academic performance analyst. When given student data, provide concise insights, identify at-risk students, and suggest specific improvement actions. Give answer only in max 60 words",
                messages=msg_history
            )
        
            while True:
                reply=response.content[0].text
                print(reply)
                msg_history.append({
                    "role":"assistant", "content": reply
                })
                ques=input("ask next question : ")
                if ques=="exit":
                    break
                msg_history.append({
                    "role":"user", "content":ques
                })
                response=client.messages.create(
                    model="claude-sonnet-4-6",
                    temperature=0.4,
                    max_tokens=1024,
                    system="You are an academic performance analyst. When given student data, provide concise insights, identify at-risk students, and suggest specific improvement actions.Give answer only in max 60 words",
                    messages=msg_history
                    
                )


        elif choice=="9":
            class1.students = load_all_students(path, classroom_id)
            summary=f"Class: {class1.name}\n"
            summary+=f"Total Students: {len(class1.students)} \n"
            summary+=f"Students: \n"
            for st in class1.students:
                summary += f"- {st.name} | {st.getPer} | {st.getGrade} \n"

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system="""You are an academic performance analyser.
                            Always respond in valid JSON only.
                            No markdown, no explanation, no extra text.
                           Just raw JSON.""",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                                                <data>
                                                {summary}
                                                </data>

                                                <task>
                                                Analyse the class and return JSON in exactly this format:
                                                {{
                                                    "top_performer": {{"name": "", "percentage": 0}},
                                                    "needs_help": {{"name": "", "percentage": 0}},
                                                    "class_average": 0,
                                                    "olympiad_candidate": "",
                                                    "overall_summary": ""
                                                }}
                                                </task>
                                                """
                    }
                ]

            )  
            #print(response.content[0].text)        
            raw = response.content[0].text.strip()
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
                raw = raw.strip()
                
            print("Raw:", raw)
            
            parsed=json.loads(raw)
            save_analysis(path,classroom_id,parsed)
            try:
                print("Top Performer: ",parsed["top_performer"]["name"])
                print("Top performer:", parsed["top_performer"]["name"])
                print("Needs help:", parsed["needs_help"]["name"])
                print("Class average:", parsed["class_average"])
                print("Olympiad candidate:", parsed["olympiad_candidate"])
            except json.JSONDecodeError as e:
                print(f"Parse failed: {e}")
                print("Raw was:", raw)

        elif choice=="10":
            
            while True:
                question=input("Ask Claude anything about your class:")
                if question.lower() == "exit":
                    break
                messages=[{"role": "user", "content":question}]
 
                while True:
                    response= client.messages.create(
                            model="claude-sonnet-4-6",
                            max_tokens=1024,
                            system=f"You are a grade tracker assistant. The current classroom_id is {classroom_id}. Always use this classroom_id when calling tools.",
                            tools=tools,
                            messages=messages
                        )
                    if response.stop_reason=="end_turn":
                        print("\n Claude: ", response.content[0].text)
                        break

                    elif response.stop_reason=="tool_use":
                        
                        for block in response.content:
                            if block.type=="tool_use":
                                tool_name=block.name
                                tool_input=block.input
                                print(f"\nClaude is calling: {tool_name}({tool_input})")

                                if tool_name=="get_all_students":
                                    result=get_all_students_tool(path,tool_input["classroom_id"])
                                elif tool_name == "get_topper":
                                    result = get_topper_tool(path, tool_input["classroom_id"])
                                elif tool_name == "get_class_average":
                                    result = get_class_average_tool(path, tool_input["classroom_id"])
                                else:
                                    result = {"error": "Unknown tool"}
                                
                                messages.append({"role":"assistant", "content":response.content })
                                messages.append({
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "tool_result",
                                            "tool_use_id": block.id,
                                            "content": json.dumps(result)
                                        }
                                    ]
                                })                           
        else:
            break

    url="https://official-joke-api.appspot.com/random_joke"
    joke=requests.get(url).json()
    print("Joke for Toppper:----> ",joke["setup"])
