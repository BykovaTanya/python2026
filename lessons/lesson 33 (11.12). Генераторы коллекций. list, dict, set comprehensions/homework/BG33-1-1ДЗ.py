scores = [5, 9, 10, 7, 8, 6]
result = [f"Студент {i}: passed" for i, score in enumerate(scores, start=1) if score >= 8]
print(result)

meetings = [("Standup", 4, 15), ("Demo", 6, 25)]
result = [f"{topic}: {members} чел, {minutes} мин" for topic, members, minutes in meetings if members < 5 and minutes <= 30]
print(result)

departments = [
    {"name": "Support", "tickets": 80, "sold": 75},
    {"name": "Analytics", "tickets": 40, "sold": 20}
]
cities = ["Moscow", "Kazan"]
availability = {
    city: "распродан" if dept['sold'] >= dept['tickets']  else "остались места"
    for dept, city in zip(departments, cities)
    if dept["tickets"] >= 50                  
}  
print(availability)






