logs = [('kate', 2), ('mike', 1), ('kate', 1), ('sofia', 3)]
finished = ['mikeв']
attempts = {}
for log in logs:
        if log in attempts:
            attempts[log] += 1
        else:
            attempts[log] = 1
        print(attempts)
def add_attempt(logs, grade):
    attempts[logs] = attempts.get(logs, 0) + grade
for student in finished:    
    delet = attempts.pop(student, "удален")
    print(f"{student}: {delet}")
print(attempts)
print("способ, рассмотренный в классе")
for name, count in logs:
    attempts[name] = attempts.get(name, 0) + count
for x in attempts:
    print(x,attempts[x])

for student in finished:
    removed = attempts.pop(student, "нет попыток")
    print(f"{student}: {removed}")
print(attempts)
