from random import choice

class Dictionary:
    
    def __init__(self):
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            self.word_list = file.read()
            self.word_list = self.word_list.split()
            # print(self.word_list)
    
    def choose(self, difficulty: int) -> str:
        list_copy = []
        for word in self.word_list:
            if len(word) == difficulty:
                list_copy.append(word)
        # print(list_copy)
        if len(list_copy) < 1:
            return ""
        return choice(list_copy)
        
if __name__ == "__main__":
    Dct = Dictionary()
    word = Dct.choose(10)
    if word == "":
        print("Brak 10-literowych słów w słowniku")
    else:
        print(word)