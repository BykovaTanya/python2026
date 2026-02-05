
       #print(f'Наибольшие продажи за {numbler_data}: {row}')
#Наибольшие продажи за 2024-10-01: Store_B с объёмом продаж 735

import csv

def analyze_sales(sales_data):
    numbler_data = input("Введите дату для отчетности (формат YYYY-MM-DD): ")

    with open('sales_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            quantity = int(row['quantity'])
            price = float(row['price'])
            biggest_sales += quantity * price

    return biggest_sales
    print(f'Наибольшие продажи за {numbler_data}: {row}')
