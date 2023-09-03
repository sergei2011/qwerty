import requests

from cours_work.number_2.util import load_random_word
from cours_work.number_2.word import Player
answer = None
filename = 'https://www.jsonkeeper.com/b/8MBE'
name = input("Ввведите имя игрока \n")

names = Player(name)
word = load_random_word(filename)
print(f"Привет, {name.title()}!")
print(f"Составьте {len(word.word_variants)} слов из слова '{word.word}'")
print("Слова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите 'stop'\nПоехали, ваше первое слово?\n")
while  names.number_word() < len(word.word_variants):
    answer = input().lower()
    word.answer = answer
    names.answer = answer
    if len(answer) > 2:
        if answer != "stop":
            if word.check_word():
                if names.checking_for_reuse():
                    print("уже использовано")
                else:
                    names.sum_word()
                    print("верно")
            else:
                print("неверно")
        else:
            break
    else:
        print("слишком короткое слово")

print(f"Игра завершена, вы угадали {names.number_word()} слов!")

