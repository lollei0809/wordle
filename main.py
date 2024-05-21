from wordfreq import top_n_list
from random import choice

words = [word for word in top_n_list('en', 1000)
         if len(word) == 5 and word.isalpha()]


class Wordle():
    def __init__(self, words):
        self.size = 5
        self.rounds_left = 6
        self.secret = ""
        self.guess = ''
        self.key = [0, 0, 0, 0, 0]

    def set_secret(self):
        self.secret = choice(words).upper()

    def set_guess(self,guess):
        if self.rounds_left > 0:
            self.guess = guess.upper()
            self.rounds_left -= 1
            self.check_guess()
            # print(self.guess)
            # print(self.key)
            if self.key == [2, 2, 2, 2, 2]:
                print(f"YAYY. word is {self.secret}")
        else:
            print(f"out of guesses. word was{self.secret}")

    def check_guess(self):
        for j in range(self.size):
            if self.guess[j] == self.secret[j]:
                self.key[j] = 2
            elif self.guess[j] in self.secret:
                self.key[j] = 1
            else:
                self.key[j] = 0

    @property
    def correct(self):
        return self.guess == self.secret

if __name__ == "__main__":
    wordle = Wordle(words)
    wordle.size = 5
    wordle.set_secret()
    # while wordle.rounds_left > 0:
    #     wordle.set_guess()
