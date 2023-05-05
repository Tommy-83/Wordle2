import random
import sys
from termcolor import colored

def print_menu():
    print("Welcome to Wordle")
    print("Type 5 letter word and hit enter")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

print_menu()
word = read_random_word()
