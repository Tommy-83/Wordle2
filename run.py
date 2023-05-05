from termcolor import colored
import random
import sys

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)

def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word below and press Enter. You have 6 tries to guess the random word.\n")


print_menu()
play_again = ""
while play_again != "q":
    word = read_random_word()
    
    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range( min(len(guess), 5) ):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempt}", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")
    play_again = input("Want to play again? Type q to exit.")
