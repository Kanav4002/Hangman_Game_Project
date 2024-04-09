import tkinter as tk
import random
from tkinter import simpledialog, messagebox

# Define themes and their respective word lists
themes = {
    "Sports": ["soccer", "basketball", "tennis", "cricket", "golf", "swimming", "athletics", "rugby", "boxing", "baseball", "tennis", "volleyball", "badminton", "hockey", "football"],
    "Fruits": ["apple", "banana", "orange", "grape", "strawberry", "kiwi", "watermelon", "pineapple", "mango", "peach"],
    "Animals": ["dog", "cat", "elephant", "tiger", "lion", "giraffe", "zebra", "monkey", "penguin", "koala", "kangaroo"]
}

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

# Define a function to choose a random word from the selected theme
def choose_word(theme):
    return random.choice(themes[theme])

# Define a function to update the hangman ASCII art
def update_hangman(mistake):
    max_mistake_index = min(len(hangman_art) - 1, mistake)
    hangman_label.config(text=hangman_art[max_mistake_index])

# Define a function to check if the letter is in the word
def check_guess(letter):
    global score
    letter = letter.lower()  # Convert to lowercase
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
    restart_button.pack()  # Display the restart button
    if player_name:
        scoreboard[player_name] = score
        display_scoreboard()

# Define a function to restart the game
def restart_game():
    global word, word_with_blanks, mistakes, score
    word = choose_word(selected_theme.get())
    word_with_blanks = ['_'] * len(word)
    word_label.config(text=' '.join(word_with_blanks))
    mistakes = 0
    score = 0  # Reset score to 0
    score_label.config(text=f"Score: {score}")  # Update score label
    guesses_left_label.config(text="Guesses Left: 6")
    update_hangman(mistakes)
    result_label.config(text="")
    for button in alphabet_buttons:
        button.config(state="normal")
    restart_button.pack_forget()  # Hide the restart button
    get_player_name()

def get_player_name():
    global player_name
    player_name = simpledialog.askstring("Player Name", "Enter your name:")
    select_theme()

def display_scoreboard():
    if scoreboard:
        sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
        scoreboard_text = "Scoreboard:\n"
        for idx, (name, score) in enumerate(sorted_scores, start=1):
            scoreboard_text += f"{idx}. {name}: {score}\n"
        messagebox.showinfo("Scoreboard", scoreboard_text)
    else:
        messagebox.showinfo("Scoreboard", "No scores recorded yet.")
        
root = tk.Tk()
root.title("HANGMAN GAME BY CODE OF DUTY")
root.configure(bg="#232427")  # Set background color to #232427

# Set initial size of the window
root.geometry("1210x600")

# Add a label to display the 'team' ASCII art with neon-green color
team_label = tk.Label(root, text=team, font=("Courier", 14), pady=10, bg="#232427", fg="#39FF14")  # Neon-green color
team_label.pack()

hangman_label = tk.Label(root, font=("Courier", 48), bg="#232427", fg="white")
hangman_label.place(relx=0.05, rely=0.5, anchor='w')  # Adjust position to the left side of the window

word_with_blanks = []

word_label = tk.Label(root, text='', font=("Arial", 24), bg="#232427", fg="white")
word_label.place(relx=0.5, rely=0.65, anchor='center')  # Adjust the values of relx and rely to move the label

# Create the score label
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16), bg="#232427", fg="#39FF14")
score_label.pack()

# Create the result label
result_label = tk.Label(root, font=("Arial", 24), bg="#232427", fg="white")
result_label.pack()

# Add label to display the number of guesses left
guesses_left_label = tk.Label(root, font=("Arial", 16), bg="#232427", fg="#39FF14")
guesses_left_label.pack()

# Create alphabet buttons
alphabet_frame = tk.Frame(root, bg="#232427")
alphabet_frame.place(relx=1.0, rely=0.2, anchor='ne', x=-20, y=100)  # Adjust position as needed

# Define column and row weights to center the buttons
for i in range(6):
    alphabet_frame.grid_columnconfigure(i, weight=1)

alphabet_buttons = []
for i in range(26):
    letter = chr(ord('a') + i)
    row = i // 5
    col = i % 5
    button = tk.Button(alphabet_frame, text=letter, font=("Arial", 14), bg="#39FF14", fg="#232427", command=lambda l=letter: check_guess(l), height=2, width=5, borderwidth=3, relief="raised")
    button.grid(row=row, column=col, sticky="nsew")  # Center-align the buttons
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

# Create a dropdown menu to select theme
selected_theme = tk.StringVar(root)
selected_theme.set("Sports")  # Default theme
def handle_theme_selection(theme):
    select_theme()
theme_menu = tk.OptionMenu(root, selected_theme, *themes.keys(), command=handle_theme_selection)
theme_menu.pack()

# Remove the duplicate packing of theme_menu
ttheme_menu = tk.OptionMenu(root, selected_theme, *themes.keys())
ttheme_menu.pack_forget()

def select_theme():
    global word, mistakes
    word = choose_word(selected_theme.get())
    word_with_blanks[:] = ['_'] * len(word)
    updated_word = ' '.join(word_with_blanks)
    word_label.config(text=updated_word)
    mistakes = 0
    guesses_left_label.config(text="Guesses Left: 6")
    update_hangman(mistakes)
    result_label.config(text="")
    for button in alphabet_buttons:
        button.config(state="normal")


# Call select_theme() initially to set up the game
select_theme()
def on_theme_change(*args):
    select_theme()

# Attach the on_theme_change function to the StringVar
selected_theme.trace_add("write", on_theme_change)
# Get player name
get_player_name()

# Start the event loop
root.mainloop()
