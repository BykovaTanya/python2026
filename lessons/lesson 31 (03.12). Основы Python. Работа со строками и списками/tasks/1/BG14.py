#a = str(input("Введите предметы через пробел: ")) #1.математика, 2.пИтон, 3.Физика
#print(a.split(","))
#print(a.strip())
dey = [1.математика, 2.пИтон, 3.Физика]
print(dey.title())
for index, item in enumerate(dey, start=1):
    print(f"{index}. {item}")



