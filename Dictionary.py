from random import choice
from Validator import Validator
from Exceptions import IllegalWord, NotAnIsogram


class Dictionary:
    def __init__(self):
        validator = Validator()
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            self.word_list = file.read()
            self.word_list = self.word_list.split()
            self.longest = self.find_longest()
            self.shortest = self.find_shortest()
            for word in self.word_list:
                if validator.validate(word) == -1:
                    raise NotAnIsogram(f"A non-isogram was inserted into the dictionary.txt file. Remove it and try again. Illegal word: {word}")
                if validator.check_for_illegal(word) is None:
                    raise IllegalWord(f"An illegal word was inserted into the dictionary.txt file. Remove it and try again. Illegal word: {word}")

    def choose(self, difficulty: int) -> str:
        list_copy = []
        for word in self.word_list:
            if len(word) == difficulty:
                list_copy.append(word)
        # print(list_copy)
        if len(list_copy) < 1:
            return ""
        return choice(list_copy)

    def find_longest(self):
        longest = 0
        for word in self.word_list:
            if len(word) > longest:
                longest = len(word)
        return longest

    def find_shortest(self):
        shortest = self.longest
        for word in self.word_list:
            if len(word) < shortest:
                shortest = len(word)
        return shortest

    def update_shor_long(self):
        self.longest = self.find_longest()
        self.shortest = self.find_shortest()


if __name__ == "__main__":
    Dct = Dictionary()
    chosen = Dct.choose(10)
    if chosen == "":
        print("Brak 10-literowych słów w słowniku")
    else:
        print(chosen)