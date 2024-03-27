import tkinter as tk
import random
from tkinter import simpledialog

# Define a list of random words
words = ["soccer","basketball","tennis","cricket","golf","swimming","athletics","rugby","boxing","baseball","tennis","volleyball","badminton","hockey","football","fencing","gymnastics","skiing","snowboarding"]

# Define the ASCII art for 'team'
team = '''
      
_________            .___               _____  ________          __          
\_   ___ \  ____   __| _/____     _____/ ____\ \______ \  __ ___/  |_ ___.__.
/    \  \/ /  _ \ / __ |/ __ \   /  _ \   __\   |    |  \|  |  \   __<   |  |
\     \___(  <_> ) /_/ \  ___/  (  <_> )  |     |    `   \  |  /|  |  \___  |
 \______  /\____/\____ |\___  >  \____/|__|    /_______  /____/ |__|  / ____|
        \/            \/    \/                         \/             \/     
'''

# Define the ASCII art for hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

# Define a function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Define a function to update the hangman ASCII art
def update_hangman(mistake):
    hangman_label.config(text=hangman_art[mistake])

# Define a function to check if the letter is in the word
def check_guess():
    global score
    letter = guess_entry.get().lower()  # Convert to lowercase
    if letter.isalpha() and len(letter) == 1:  # Ensure it's a single lowercase letter
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_with_blanks[i] = letter
                    score += 5 # Increment score by 5 for each correct alphabet
                    score_label.config(text=f"Score: {score}")  # Update score label for each correct alphabet
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
        guess_entry.delete(0, tk.END)  # Clear the entry after each guess
        disable_alphabet_button(letter)

# Define a function to disable alphabet button after it's clicked
def disable_alphabet_button(letter):
    alphabet_buttons[ord(letter) - ord('a')].config(state=tk.DISABLED)  # Disable the button

# Define a function to end the game
def end_game(result):
    global player_name
    if result == "win":
        result_text = "You win!"
    else:
        result_text = "You Lose, the word was " + word
    result_label.config(text=result_text)
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")
    restart_button.pack()  # Display the restart button
    if player_name:
        scoreboard[player_name] = score
        display_scoreboard()

# Define a function to restart the game
def restart_game():
    global word, word_with_blanks, mistakes, score
    word = choose_word()
    word_with_blanks = ['_'] * len(word)
    word_label.config(text=' '.join(word_with_blanks))
    mistakes = 0
    score = 0  # Reset score to 0
    score_label.config(text=f"Score: {score}")  # Update score label
    guesses_left_label.config(text="Guesses Left: 6")
    update_hangman(mistakes)
    result_label.config(text="")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    for button in alphabet_buttons:
        button.config(state="normal")
    restart_button.pack_forget()  # Hide the restart button
    get_player_name()

def get_player_name():
    global player_name
    player_name = simpledialog.askstring("Player Name", "Enter your name:")

def display_scoreboard():
    if scoreboard:
        sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
        scoreboard_text = "Scoreboard:\n"
        for idx, (name, score) in enumerate(sorted_scores, start=1):
            scoreboard_text += f"{idx}. {name}: {score}\n"
        tk.messagebox.showinfo("Scoreboard", scoreboard_text)
    else:
        tk.messagebox.showinfo("Scoreboard", "No scores recorded yet.")

root = tk.Tk()
root.title("HANGMAN GAME BY CODE OF DUTY")
root.configure(bg="black")  # Set background color to black

# Set initial size of the window
root.geometry("1210x600")

# Add a label to display the 'team' ASCII art with neon-green color
team_label = tk.Label(root, text=team, font=("Courier", 14), pady=10, bg="black", fg="#39FF14")  # Neon-green color
team_label.pack()

# Add a label to display the theme
theme_label = tk.Label(root, text="Theme: Sports", font=("Arial", 16), bg="black", fg="#39FF14")
theme_label.pack()

hangman_label = tk.Label(root, font=("Courier", 16), bg="black", fg="white")
hangman_label.pack()

word = choose_word()
word_with_blanks = ['_'] * len(word)
word_label = tk.Label(root, text=' '.join(word_with_blanks), font=("Arial", 24), bg="black", fg="white")
word_label.pack()

# Create the guess entry and button
guess_entry_frame = tk.Frame(root, bg="black")
guess_entry_frame.pack()
guess_entry = tk.Entry(guess_entry_frame, width=3, font=("Arial", 24), bg="black", fg="white")
guess_entry.pack(side="left", padx=5, pady=5)
guess_button = tk.Button(guess_entry_frame, text="Guess", command=check_guess, bg="black", fg="black")  # Change color to black
guess_button.pack(side="left", padx=5, pady=5)

# Create the score label
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16), bg="black", fg="white")
score_label.pack()

# Create the result label
result_label = tk.Label(root, font=("Arial", 24), bg="black", fg="white")
result_label.pack()

# Add label to display the number of guesses left
guesses_left_label = tk.Label(root, font=("Arial", 16), bg="black", fg="#39FF14")
guesses_left_label.pack()

# Create alphabet buttons
alphabet_frame = tk.Frame(root, bg="black")
alphabet_frame.pack(side="bottom", pady=20)  # Place at the bottom with some padding
alphabet_buttons = []
for i in range(26):
    letter = chr(ord('a') + i)
    button = tk.Button(alphabet_frame, text=letter, font=("Arial", 12), bg="white", fg="black", command=check_guess)
    button.grid(row=0, column=i, padx=2, pady=2)
    alphabet_buttons.append(button)

# Initialize the game
mistakes = 0
update_hangman(mistakes)
guesses_left_label.config(text="Guesses Left: 6")  # Initial guesses left value

# Create restart button
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack()
restart_button.pack_forget()  # Initially hide the restart button

# Initialize player name and scoreboard
player_name = None
scoreboard = {}

# Get player name
get_player_name()

# Start the event loop
root.mainloop()
