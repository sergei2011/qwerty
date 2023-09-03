from util import Question, load_test
score = 0
count = 0

print("Игра начинается!")

quest_list = load_test()
for i in range(len(load_test())):
    s =Question(quest_list[i]['q'], int(quest_list[i]['d']), int(quest_list[i]['a']))
    s.user_response = int(input(s.build_question()))
    print(s.build_feedback())
    score += s.get_points()
    if s.is_correct():
        count += 1


print(f"Вот и все!\nОтвечено {count} вопроса из {len(load_test())}\nНабрано баллов: {score}")
