import random
import sys
from termcolor import colored, cprint

def print_menu():
    print("Welcome to Wordle")
    print("Type 5 letter word and hit enter")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

print_menu()
word = read_random_word()

for attempt in range(1, 7):
    guess = input().lower()

    for i in range( min(len(guess), 5) ):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")

        if guess == word:
            print(colored(f"Congrats! YOu got the wordle in {i}", 'red'))

        
