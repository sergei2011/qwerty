def get_grade(grade):
    estimation = {"2": "Плохо",
                  "3": "Удовлетворительно",
                  "4": "Хорошо",
                  "5": "Отлично"}
    if grade in estimation:
        return estimation[grade]
    else:
        return "Ошибка"

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")
#print(get_grade(input(56)))

# print(grade, '-', get_grade())
