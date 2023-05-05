import random

def print_menu():
    print("Welcome to Wordle")
    print("Type 5 letter word and hit enter")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return

print_menu()

