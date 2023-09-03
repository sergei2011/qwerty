import json
import requests
import random
from word import BasicWord

#filename = "word.json"
n = None



def load_random_word(filename):
    """"создаем функцию для получение случайного слова и его производных"""
    list_word = requests.get(filename)
    set_words = list_word.json()
    random.shuffle(set_words)
    play = BasicWord(set_words[1]['word'], set_words[1]['subwords'])
    return (play)

#print(filename)
#print(load_random_word('https://www.jsonkeeper.com/b/8MBE'))
