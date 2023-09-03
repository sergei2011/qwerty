import json
import random
filename = "question.json"
class Question:

    def __init__(self, question, complexity, answer):
        """"– текст вопроса
              – сложность вопроса
              – верный вариант ответа

              – задан ли вопрос (по умолчанию False)
              – ответ пользователя (по умолчанию None)
              – баллы за вопрос (вычисляется в момент инициализации)
              """
        self.question = question
        self.complexity = complexity
        self.answer = answer

        self.user_response = None
        self.points = self.complexity * 10



    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.points = self.points * self.is_correct()

        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        return self.user_response == self.answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        self.question = f"Вопрос: {self.question}\nСложность {self.complexity}/5\n"

            #self.question = f"Вопрос: {load_test()[i]['q']}\nСложность {load_test()[i]['d']}/5"
        return self.question




    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов"

        else:
            return f"Ответ неверный, верный ответ {self.answer}"


def load_test():
    with open(filename) as f:
        list_of_ques = json.load(f)

    questions = []
    for quest in list_of_ques:
        questions.append(quest)
    random.shuffle(questions)
    return questions


#print(load_test()[1])