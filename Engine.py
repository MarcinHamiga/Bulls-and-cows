from Dictionary import Dictionary
from Validator import Validator
from Stats import Stats
import datetime


class Engine:
    def __init__(self):
        self.dict = Dictionary()
        print(self.dict.word_list)
        self.validator = Validator()
        self.is_running = True

        # Settings variables
        self.difficulty = 4
        self.tries = 10
        self.tries_left = 10
        self.save_score = False
        # Game variables
        self.secret_word = ""
        self.previous_guesses = []

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

    def settings_screen(self):
        self.settings_command()

    def show_settings(self):
        print(f"Poziom trudności: {self.difficulty}")
        print(f"Liczba prób: {self.tries}")
        if self.save_score is True:
            print("Zapisz wynik: Tak")
        else:
            print("Zapisz wynik: Nie")
        print(f"\nWpisz 'trudność' aby zmienić poziom trudności\nWpisz 'próby' aby zmienić liczbę prób\n"
              f"Wpisz 'powrót' aby wrócić do menu głównego\nWpisz 'dodaj' aby dodać własne słowo do słownika\n"
              f"Wpisz 'najlepsze' aby włączyć/wyłączyć zapisywanie wyników do pliku tekstowego.")

    def settings_command(self):
        settings = True
        while settings:
            self.show_settings()
            cmd = input("> ")
            if cmd.lower() == "trudność":
                while True:
                    try:
                        self.difficulty = int(input(f"Ile liter ma mieć hasło? (nie więcej niż {self.dict.longest})\n> "))
                        self.fix_long_shor()
                        break
                    except:
                        print("Proszę wpisać liczbę.")
            if cmd.lower() == "próby":
                while True:
                    try:
                        self.tries = int(input(f"Ile prób chcesz mieć?\n> "))
                        self.fix_tries()
                        break
                    except:
                        print("Proszę wpisać liczbę.")
            if cmd.lower() == "powrót":
                settings = False
            if cmd.lower() == "dodaj":
                self.add_word()
            if cmd.lower() == "najlepsze":
                self.config_save_score()

    def config_save_score(self):
        if self.save_score is True:
            self.save_score = False
        else:
            self.save_score = True

    def add_word(self):
        while True:
            word = input("Wpisz słowo które chcesz dodać.\n> ")
            word = self.validator.check_for_illegal(word)
            if word is None:
                print("Wpisz słowo które zawiera WYŁĄCZNIE litery.")
            elif self.validator.validate(word) == -1:
                print("Wpisz słowo które jest izogramem.")
            elif word in self.dict.word_list:
                print("Podane słowo już jest w słowniku.")
            else:
                with open("dictionary.txt", "a") as file:
                    file.write(f" {word}".rstrip('\n'))
                self.dict.word_list.append(word)
                break

    def fix_tries(self):
        if self.tries < 1:
            print("Przekroczono minimalną liczbę prób; automatycznie ustawiono liczbę prób na 1.")
            self.tries = 1

    def rules_screen(self):
        print("""Bulls & Cows to tekstowa gra w której komputer losuje słowo, które jest izogramem (słowem, w którym żadna litera nie występuje więcej niż raz), a zadaniem gracza jest zgadnąć słowo wylosowane przez komputer.
Gracz zna długość ukrytego słowa a po każdej próbie odgadnięcia go informowany jest o liczbie liter w odpowiedzi, 
które znajdują się w wylosowanym słowie, jednak na innej pozycji niż w odpowiedzi (cows)
oraz informowany jest o ilości liter, które znajdują się w odpowiedzi na tej samej pozycji co w odpowiedzi (bulls). 
Gracz widzi również ile prób odpowiedzi mu pozostało.
Gra kończy się w momencie w którym ilość bulls zrówna się z długością ukrytego słowa (co oznacza, że gracz odnalazł ukryte słowo) lub gdy liczba prób spadnie do wartości 0.\n\n""")

    def fix_long_shor(self):
        if self.difficulty > self.dict.longest:
            print("Przekroczono maksymalną liczbę liter; automatycznie ustawiono maksymalną dopuszczalną wartość.")
            self.difficulty = self.dict.longest
        if self.difficulty < self.dict.shortest:
            print("Przekroczono minimalną liczbę liter; automatycznie ustawiono minimalną dopuszczalną wartość.")
            self.difficulty = self.dict.shortest

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
            if self.save_score is True:
                self.save_results()
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

    def check_word(self, player_input):
        player_input = self.validator.check_for_illegal(player_input)
        if player_input is None:
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

    def save_results(self):
        try:
            with open("highscores.txt", "a") as file:
                file.write(f"{datetime.datetime.now()} - słowo: {self.secret_word}, pozostałych prób: {self.tries_left} z {self.tries}\n")
        except FileNotFoundError:
            with open("highscores.txt", "w") as file:
                file.write(f"{datetime.datetime.now()} - słowo: {self.secret_word}, pozostałych prób: {self.tries_left} z {self.tries}\n")