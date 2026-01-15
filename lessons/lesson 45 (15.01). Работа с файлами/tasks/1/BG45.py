try:
    with open("BG45.txt", "r", encoding="utf-8") as file:
    #content = file.read()
        for line in file:
            if  line.strip():
                print(line.strip())
    #print(file)
except FileNotFoundError:
    print("Файл не найден.")
except IOError:
    print("Ошибка ввода-вывода.")            
