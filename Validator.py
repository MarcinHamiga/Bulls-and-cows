import re


class Validator:
    regex = r"^[a-zA-ZąĄęĘóÓłŁżŻźŹćĆńŃśŚ]+$"

    @staticmethod
    def validate(word):
        split_word = [char for char in word]
        if len(split_word) != len(set(split_word)):
            return -1
        return 0

    def check_for_illegal(self, player_input):
        test = re.search(self.regex, player_input)
        if test:
            return player_input.upper()
        else:
            return None
    
    
if __name__ == "__main__":
    vali = Validator()
    print(vali.validate("KREW"))