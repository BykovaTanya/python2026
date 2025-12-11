courses = [
    {"title": "Python старт", "students": 10, "status": "open"},
    {"title": "Git базовый", "students": 4, "status": "open"},
    {"title": "SQL практика", "students": 12, "status": "closed"},
    {"title": "Async Python", "students": 8, "status": "open"}
]
open_groups = {
    course["title"]: course["students"]
    for course in courses
    if course["status"] == "open"
        if 5< course["students"] <=15
}
print(open_groups)
