import tkinter as tk
import random

#define a list of random words
words = ["soccer","basketball","tennis","cricket","golf","swimming","athletics","rugby","boxing","baseball","tennis","volleyball","badminton","hockey","football","fencing","gymnastics","skiing","snowboarding"]

#define the ASCII art for 'team'
team = '''
      
_________            .___               _____  ________          __          
\_   ___ \  ____   __| _/____     _____/ ____\ \______ \  __ ___/  |_ ___.__.
/    \  \/ /  _ \ / __ |/ __ \   /  _ \   __\   |    |  \|  |  \   __<   |  |
\     \___(  <_> ) /_/ \  ___/  (  <_> )  |     |    `   \  |  /|  |  \___  |
 \______  /\____/\____ |\___  >  \____/|__|    /_______  /____/ |__|  / ____|
        \/            \/    \/                         \/             \/     
'''

#define the ASCII art for hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

#define a function to choose a random word from the list
def choose_word():
    return random.choice(words)

#define a function to update the hangman ASCII art
def update_hangman(mistake):
    hangman_label.config(text=hangman_art[mistake])

#define a function to check if the letter is in the word
def check_guess():
    letter = guess_entry.get().lower()  # Convert to lowercase
    if letter.isalpha() and len(letter) == 1:  # Ensure it's a single lowercase letter
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_with_blanks[i] = letter
            word_label.config(text=' '.join(word_with_blanks))
            if '_' not in word_with_blanks:
                end_game("win")
        else:
            global mistakes
            mistakes += 1
            guesses_left_label.config(text=f"Guesses Left: {6 - mistakes}")  # Update guesses left label
            update_hangman(mistakes)
            if mistakes == 6:
                end_game("lose")
        alphabet_buttons[ord(letter) - ord('a')].config(bg="gray", state=tk.DISABLED)  # Change color and disable button

def end_game(result):
    if result == "win":
        result_text = "You win!"
    else:
        result_text = "You Lose, the word was " + word
    result_label.config(text=result_text)
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")
    for button in alphabet_buttons:
        button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("HANGMAN GAME BY CODE OF DUTY")
root.configure(bg="black")  # Set background color to black

# Set initial size of the window
root.geometry("1210x600")  # Set initial size to 800x600 pixels

# Add a label to display the 'team' ASCII art with neon-green color
team_label = tk.Label(root, text=team, font=("Courier", 14), pady=10, bg="black", fg="#39FF14")  # Neon-green color
team_label.pack()

hangman_label = tk.Label(root, font=("Courier", 16), bg="black", fg="white")
hangman_label.pack()

word = choose_word()
word_with_blanks = ['_'] * len(word)
word_label = tk.Label(root, text=' '.join(word_with_blanks), font=("Arial", 24), bg="black", fg="white")
word_label.pack()

#create the guess entry and button
guess_entry_frame = tk.Frame(root, bg="black")
guess_entry_frame.pack()
guess_entry = tk.Entry(guess_entry_frame, width=3, font=("Arial", 24), bg="black", fg="white")
guess_entry.pack(side="left", padx=5, pady=5)
guess_button = tk.Button(guess_entry_frame, text="Guess", command=check_guess, bg="black", fg="black")  # Change color to black
guess_button.pack(side="left", padx=5, pady=5)

#create the result label
result_label = tk.Label(root, font=("Arial", 24), bg="black", fg="white")
result_label.pack()

# Add label to display the number of guesses left
guesses_left_label = tk.Label(root, font=("Arial", 16), bg="black", fg="white")
guesses_left_label.pack()

# Create alphabet buttons
alphabet_frame = tk.Frame(root, bg="black")
alphabet_frame.pack(side="bottom", pady=20)  # Place at the bottom with some padding
alphabet_buttons = []
for i in range(26):
    letter = chr(ord('a') + i)
    button = tk.Button(alphabet_frame, text=letter, font=("Arial", 12), bg="white", fg="black", state=tk.NORMAL,
                       command=lambda l=letter: on_alphabet_click(l))
    button.grid(row=0, column=i, padx=2, pady=2)
    alphabet_buttons.append(button)

def on_alphabet_click(letter):
    alphabet_buttons[ord(letter) - ord('a')].config(bg="gray", state=tk.DISABLED)  # Change color and disable button
    check_guess()

# Initialise the game
mistakes = 0
update_hangman(mistakes)
guesses_left_label.config(text="Guesses Left: 6")  # Initial guesses left value

# Start the event loop
root.mainloop()