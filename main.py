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

    def set_guess(self, guess):
        if self.rounds_left > 0:
            self.guess = guess.upper()
            self.rounds_left -= 1
            self.check_guess()
            # print(self.guess)
            # print(self.key)
        else:
            print(f"out of guesses. word was{self.secret}")

    def check_guess(self):
        temp_guess = list(self.guess)
        temp_secret = list(self.secret)
        for j in range(self.size):
            if temp_guess[j] == temp_secret[j]:
                self.key[j] = 2
                temp_guess[j] = "*"
                temp_secret[j] = "*"
        for i, letter in enumerate(temp_guess):
            if letter != "*" and letter in temp_secret:
                self.key[i] = 1
                temp_secret[temp_secret.index(letter)] = "*"
            elif temp_guess[i] != "*":
                self.key[i] = 0

    @property
    def correct(self):
        return self.guess == self.secret


if __name__ == "__main__":
    wordle = Wordle(words)
    wordle.size = 5
    wordle.set_secret()
    # while wordle.rounds_left > 0:
    #     wordle.set_guess()
