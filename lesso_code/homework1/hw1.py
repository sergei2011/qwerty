import random  # вызов random

# объявление переменных
word_dic = {}
score = 0
name_gamer = input("Введите ваше имя  \n ")


def read_word():
    """
    создаем функцию для создания словаря
    из слова и измененного слова
    :return:
    """
    with open("words.txt", "r") as f:
        for line in f:
            words = line.strip()
            a = list(words)
            random.shuffle(a)
            word_dic[''.join(a)] = words

        return word_dic

 
def write_top():
    """
    создаем функцию записи имени игрока и его очков
    :return:
    """
    with open("history.txt", "a") as f:
        f.write(name_gamer)
        f.write(f"   {str(score)}\n")


def read_top():
    """
    создаем функцию по подсчету количества записей и определению максимального количества очков
    :return:
    """
    count_line = 0
    score_top = 0
    with open("history.txt", "r") as f:
        for line in f:
            count_line += 1
            line_spl = line.split()
            if int(line_spl[1]) > score_top:
                score_top = int(line_spl[1])
    return count_line, score_top


# ВЫзываем функцию со словами и задаем их пользователю
for riddle in read_word():
    answer = input(f"Угадайте слово: {riddle}   ")
    if answer.lower() == word_dic[riddle]:
        score += 10
        print("Верно! Вы получаете 10 очков.")

    else:
        print(f"Неверно! Верный ответ – {word_dic[riddle]}.")

write_top()
number, score_max = read_top()
print(f"Всего игр сыграно: {number} \nМаксимальный рекорд: {score_max}")
