🎮 Hangman Game (Python)
📖 Overview

This project is a console-based Hangman game built in Python. The game randomly selects a hidden word from a word list, and the player must guess the letters one at a time before running out of lives.
Each incorrect guess reduces the player's remaining lives and gradually reveals the Hangman drawing. The objective is to successfully guess the entire word before all lives are lost.
Hangman is a classic word-guessing game where players reveal letters of a hidden word while avoiding too many incorrect guesses.

✨ Features

- Random word selection from a word list
- Letter-by-letter guessing system
- Displays the hidden word using placeholders (_)
- Tracks previously guessed letters
- Life system that decreases with incorrect guesses
- ASCII Hangman stages that update after wrong guesses
- Clear win and lose conditions


🧠 How It Works

- The program randomly selects a word from a predefined list.
- The game displays blanks (_) representing each letter of the word.
- The player guesses one letter at a time.
- Correct guesses reveal the letter in its correct position.
- Incorrect guesses reduce the player's remaining lives.
- The player wins if the word is fully revealed before lives reach zero, otherwise the player loses.


📂 Project Structure
hangman/
│
├── main.py            # Main game logic
├── hangman_words.py   # Word list used in the game
├── hangman_art.py     # ASCII art for the hangman and logo
└── README.md


🛠 Technologies Used

- Python 
- Python standard library (random)
- Basic programming concepts:
  - loops (for, while)
  - conditionals
  - lists and strings
    

🎯 Example Output
Word to guess: _____
6/6 LIVES LEFT

Guess a letter: c
c____


👨‍💻 Author
Mohammed Jonaed Haque
