from Dictionary import Dictionary
from Validator import Validator
from Stats import Stats
import re

class Engine:
    def __init__(self):
        self.dict = Dictionary()
        self.validator = Validator()
        self.is_running = True
        self.regex = r"^[a-zA-ZąĄęĘóÓłŁżŻźŹćĆńŃśŚ]+$"
        # Settings variables
        self.difficulty = 4
        self.tries = 10
        self.tries_left = 10
        # Game variables
        self.secret_word = ""
        self.previous_guesses = []
        self.player_input = ""
    
        
    def main(self):
        while self.is_running:
            self.show_menu()
            self.main_command()
    
    
    def main_command(self):
        cmd = input("> ")
        if cmd == "1":
            self.new_game()
            self.game_screen()
        elif cmd == "2":
            self.rules_screen()
        elif cmd == "3":
            self.settings_screen()
        elif cmd == "4":
            exit()
        else:
            print("Komenda nie istnieje")
    
    
    def show_menu(self):
        print("Bulls & Cows")
        print("1 - Nowa Gra")
        print("2 - Zasady Gry")
        print("3 - Ustawienia")
        print("4 - Koniec")
    
        
    def game_screen(self):
        print(self.secret_word)
        while True:
            if self.check_lose() == 1:
                break
            print(f"Odgadnij sekretne słowo składające się z {self.difficulty} liter")
            self.print_tries()
            while True:
                result = self.check_word(self.take_input())
                if isinstance(result, Stats):
                    break
                else:
                    print("Wprowadz odpowiedź zawierającą WYŁĄCZNIE litery")       
            result.show_stats()
            self.take_try()
            if self.check_win(result) == 1:
                break


    def new_game(self):
        self.tries_left = self.tries
        self.secret_word = self.dict.choose(self.difficulty)
    
    
    def check_win(self, result):
        if result.get_bulls() == self.difficulty:
            print("Wygrałeś!")
            input("---Naciśnij enter aby wrócić do menu głównego---")
            return 1
        else:
            return 0
    
        
    def check_lose(self):
        if self.tries == 0:
            print("Przegrałeś!")
            input("---Naciśnij enter aby wrócić do menu głównego---")
            return 1
        else:
            return 0   
    
        
    def take_input(self):
        while True:
            player_input = input("> ")
            if self.validator.validate(player_input) == -1:
                print("Odpowiedź musi być izogramem!")
            elif len(player_input) == self.difficulty:
                return player_input
            else:
                print(f"Odpowiedź musi mieć tyle samo liter co sekretne słowo! To znaczy {self.difficulty}.")
    
    
    def split_to_letters(self, word):
        return [char for char in word]
    
    
    def check_for_illegal(self, player_input):
        test = re.search(self.regex, player_input)
        if test:
            return player_input.upper()
        else:
            return None
    
    
    def check_word(self, player_input):
        player_input = self.check_for_illegal(player_input)
        if player_input == None:
            return None
        bulls = 0
        cows = 0
        secret_chars = self.split_to_letters(self.secret_word)
        input_chars = self.split_to_letters(player_input)
        for char in input_chars:
            print(char)
            if char in secret_chars:
                if input_chars[input_chars.index(char)] == secret_chars[input_chars.index(char)]:
                    bulls += 1
                else:
                    cows += 1
        return Stats(bulls, cows)
    
    
    def take_try(self):
        self.tries_left -= 1
        
        
    def print_tries(self):
        print(f"Pozostało {self.tries_left} prób")
        
if __name__ == "__main__":
    game = Engine()
    game.main()