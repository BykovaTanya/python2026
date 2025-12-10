rehearsals = ["ПН.строй", "ВТ.динамика", "СР.ансамбль", "ЧТ.солисты"]
extra = ["ПТ.общий прогон", "СБ.работа с дирежером"]
rehearsals.extend(extra)
print(rehearsals)
for repetition in rehearsals:  
    print(repetition)
rehearsals.insert(2, "Мастер-класс по дыханию")
print(rehearsals)
removed = rehearsals.pop(4)
#rehearsals.remove("ЧТ.солисты")# ели удалить по значениею, но вывести в принт неполучается
print(f"Отменен из-за болезни солиста {removed}")
displaced = rehearsals.pop(0)
middle = len(rehearsals) // 2
rehearsals.insert(middle, displaced)
print(rehearsals)
for repetition in rehearsals:  
    print(repetition)
