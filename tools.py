tools=[
    {
        "name": "get_all_students",
        "description": " Get All students in classroom with their marks and grades",
        "input_schema": {
            "type": "object",
            "properties":{
                "classroom_id":{
                    "type": "integer",
                    "description":"The ID of the classroom "
                }
            },
        "required":["classroom_id"]
        }
    },
    {
        "name":"get_topper",
        "description": "Get top performing student from class",
        "input_schema": {
            "type": "object",
            "properties":{
                "classroom_id":{
                    "type":"integer",
                    "description":"The ID of the classroom"
                }
            },
        "required":["classroom_id"]
        }
    },
    {
        "name":"get_class_average",
        "description": "Get the average marks of classroom",
        "input_schema":{
            "type":"object",
            "properties":{
                "classroom_id":{
                    "type":"integer",
                    "description":"The ID of the classroom"
                }
            },
        "required":["classroom_id"]
        }
    }
]