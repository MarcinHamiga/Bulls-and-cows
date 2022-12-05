class Stats:
    bulls = None
    cows = None
    
    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows
    
    def show_stats(self):
        print(f"Bulls = {self.bulls} | Cows = {self.cows}\n\n")
        
    def get_bulls(self):
        return self.bulls
