class BasicWord:
    def __init__(self, word, word_variants):
        self.word = word
        self.word_variants = word_variants

        self.answer = None

    def __repr__(self):
        return (f"слово {self.word} варианты слов{self.word_variants}")



    def check_word(self):
        """"проверку введенного слова в списке допустимых подслов"""
        if self.answer in self.word_variants:
            return True

    def sum_word(self):
        """"подсчет количества подслов"""
        return len(self.word_variants)


class Player:
    def __init__(self, name_player, word_player = []):
        self.name_player = name_player
        self.word_player = word_player

        self.answer = None

    def __repr__(self):
        return (f"Имя {self.name_player}   Использованные слова {self.word_player}")

    def number_word(self):
        """"получение количества использованных слов"""
        return len(self.word_player)

    def sum_word(self):
        """"добавление слова в использованные слова"""
        self.word_player.append(self.answer)

    def checking_for_reuse(self):
        """"проверка использования данного слова до этого """
        return self.answer in self.word_player

#s = BasicWord("ghjkgik", ["gkjhnjkl", "gjkholjo", "jho"])
#s = Player("ghjkgik", ["gkjhnjkl", "gjkholjo", "jho"])
#print(s)
