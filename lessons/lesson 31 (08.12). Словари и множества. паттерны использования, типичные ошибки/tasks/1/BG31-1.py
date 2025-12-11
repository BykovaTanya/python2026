rooms = [
    ('piano-1', 'Ирина'),
    ('strings-2', 'Олег'),
    ('drums-1', 'Света'),
]
today_room = 'strings-2'
free_room = 'theory-3'
last_teacher = dict(rooms)
print(last_teacher)
today_room = last_teacher.get('strings-2', 0)
print(today_room)
print(last_teacher.get("free_room", "свободен"))
