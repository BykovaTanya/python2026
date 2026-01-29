import csv

def students(ball):
    with open('students.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        sredniy_ball = map(lambda ocenki: sum(ocenki) / len(ocenki),ball)

    return sredniy_ball
