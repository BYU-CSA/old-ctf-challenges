import random


from collections import Counter
from os import system


class color:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[00m'

    def print(self, printing_thing, clr='\033[00m', end="\n"):
        print(f"{clr}{printing_thing}{color.reset}", end=end)
    
    def clear():
        system('clear')


class Guess:
    def __init__(self, guess, real):
        # Green means right letter, right place
        # Yellow means right letter, wrong place
        # Grey means no more of that letter
        letter_counter = Counter(real)
        self.guess = guess
        status = ['x']*len(real)

        for i, (g, r) in enumerate(zip(guess, real)):
            if g == r:
                letter_counter.subtract(g)
                # Right letter, right place
                status[i] = 'g'
        
        for i, g in enumerate(guess):
            if status[i] == 'x':
                if letter_counter[g] > 0:
                    # Right letter, wrong place
                    status[i] = 'y'
                    letter_counter.subtract(g)
        
        self.status = ''.join(status)
    
    def __str__(self):
        # return self.guess + "\n" + self.status
        color_map = {
            'x': color.red,
            'y': color.yellow,
            'g': color.green,
        }
        return ''.join(f"{color_map[s]}{g}" for g, s in zip(self.guess, self.status)) + color.reset


class Wordle:
    def __init__(self):

        self.large_dictionary = list(line.strip() for line in open("large.txt"))
        self.small_dictionary = list(line.strip() for line in open("small.txt"))
        self.flag = open("flag.txt").readlines()[0].strip()

        self.word = ""
        self.user_word = ""
        self.previous_guesses = []
        self.debug = []
        self.error = None

        self.choose_word()
        self.running = False
        self.win = False

        self.tries = 12

        self.inputs = [
            self.user_input,
        ]
        self.calculates = [
            self.clear_error,
            self.validate_guess,
            self.evaluate_guess,
            self.determine_tries,
        ]
        self.draws = [
            color.clear,
            self.draw_title,
            self.draw_guesses,
            self.draw_tries_left,
            self.draw_win,
            self.draw_error,
            self.draw_debug,
        ]


    def choose_word(self):
        self.word = random.choice(self.small_dictionary)


    def loop(self):
        self.input_()
        self.calculate()
        self.draw()


    def input_(self):
        for inp in self.inputs:
            inp()


    def calculate(self):
        for calc in self.calculates:
            calc()


    def draw(self):
        for dr in self.draws:
            dr()


    def user_input(self):
        self.user_word = input(">>> ").strip().lower()


    def clear_error(self):
        self.error = None


    def validate_guess(self):
        if self.error:
            return
        if self.user_word not in self.large_dictionary:
            self.error = self.user_word + ": Not a valid word"
            return


    def evaluate_guess(self):
        if self.error:
            return
        self.previous_guesses.append(Guess(self.user_word, self.word))
        if self.user_word == self.word:
            self.win = True
            self.running = False
    

    def determine_tries(self):
        if len(self.previous_guesses) == self.tries:
            self.running = False


    def draw_title(self):
        print("WORDLE\n")


    def draw_guesses(self):
        for guess in self.previous_guesses:
            print(guess)


    def draw_tries_left(self):
        for i in range(self.tries - len(self.previous_guesses)):
            print("_____")


    def draw_win(self):
        if self.win:
            print(self.flag)
        elif not self.running:
            print(f"The word was {self.word}")


    def draw_error(self):
        if self.error:
            print(self.error)


    def draw_debug(self):
        for i in self.debug:
            print(i)
        self.debug = []


    def run(self):
        self.running = True
        self.draw()
        while self.running:
            self.loop()


def main():
    wordle = Wordle()
    wordle.run()
    # print(Guess('heyyo', 'hello'))
    

if __name__ == "__main__":
    main()