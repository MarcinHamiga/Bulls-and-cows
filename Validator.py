class Validator:
    
    def validate(self, word):
        split_word = [char for char in word]
        if len(split_word) != len(set(split_word)):
            return -1
        return 0
    
    
if __name__ == "__main__":
    vali = Validator()
    print(vali.validate("KREW"))