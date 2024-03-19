import random
import os
import time
from threading import Thread
from colorama import Fore, Style

efecnblt = ['''
      
_________            .___               _____  ________          __          
\_   ___ \  ____   __| _/____     _____/ ____\ \______ \  __ ___/  |_ ___.__.
/    \  \/ /  _ \ / __ |/ __ \   /  _ \   __\   |    |  \|  |  \   __<   |  |
\     \___(  <_> ) /_/ \  ___/  (  <_> )  |     |    `   \  |  /|  |  \___  |
 \______  /\____/\____ |\___  >  \____/|__|    /_______  /____/ |__|  / ____|
        \/            \/    \/                         \/             \/     
''']

hangman = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

word_list = ["soccer",
    "basketball",
    "tennis",
    "cricket",
    "golf",
    "swimming",
    "athletics",
    "rugby",
    "boxing",
    "baseball",
    "tennis",
    "volleyball",
    "badminton",
    "hockey",
    "football",
    "fencing",
    "gymnastics",
    "skiing",
    "snowboarding"]

chosen_word = random.choice(word_list)

os.system("clear")

# Function to print ASCII art with animation effect
def print_animation(art_list, delay=0.1):
    for frame in art_list:
        print(frame)
        time.sleep(delay)

# Timer function
def timer(seconds):
    print(Fore.YELLOW + "\nStarting game in:")
    for i in range(seconds, 0, -1):
        print(Fore.YELLOW + f"{i} ", end="", flush=True)
        time.sleep(1)
    print()

# Starting the timer for 3 seconds
timer_thread = Thread(target=timer, args=(3,))
timer_thread.start()

# Printing ASCII art with animation after timer
timer_thread.join()
print_animation(efecnblt)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(Fore.CYAN + "\n" + " ".join(alphabet) + "\n")

screen = ["_"] * len(chosen_word)
print(Fore.BLUE + f"\t\t{' '.join(screen)}" + Style.RESET_ALL)
print(Fore.CYAN + hangman[0])

guessed = []
counter = 6

while True:
    guess_a_word = input("\nGuess a word: ").lower()
    os.system("clear")

    if guess_a_word in guessed:
        print(Fore.RED + f"\t\tYou already guessed '{guess_a_word}'!" + Style.RESET_ALL)
    elif guess_a_word not in guessed:
        if guess_a_word not in chosen_word:
            counter -= 1
        guessed.append(guess_a_word)

    for i, letter_in_word in enumerate(chosen_word):
        if guess_a_word == letter_in_word:
            screen[i] = guess_a_word

    for i, letter_in_alphabet in enumerate(alphabet):
        if guess_a_word == letter_in_alphabet:
            alphabet[i] = "-"

    guessed.append(guess_a_word)

    print(Fore.GREEN + f"\n{' '.join(efecnblt)}\n")
    print(Fore.CYAN + " ".join(alphabet) + "\n")
    print(Fore.BLUE + f"\t\t{' '.join(screen)}" + Style.RESET_ALL)

    if counter > 0:
        print(Fore.CYAN + hangman[6 - counter])
    else:
        print(Fore.CYAN + hangman[6])
        print(Fore.RED + "\n\n-------YOU LOST!--------\n")
        print(Fore.RED + f"The answer was --->  {chosen_word}\n" + Style.RESET_ALL)
        break

    if "_" not in screen:
        print(Fore.MAGENTA + "\n\nCongratulations!\nYOU WON THE GAME :)\n" + Style.RESET_ALL)
        break