# 🎯 Hangman Game (Python)

A classic **Hangman** word-guessing game built in Python for the console. Guess the hidden word one letter at a time before running out of lives — complete with ASCII art visuals for each wrong guess!

This project was built as part of the **CodeAlpha Internship** program.

## 📌 Features

- 🎲 Random word selection from a predefined word list
- 🖼️ ASCII art hangman stages that update with each incorrect guess
- ✅ Real-time display of guessed letters and word progress (e.g. `p _ t h _ n`)
- 🛡️ Robust input validation (rejects invalid characters, repeated guesses, multi-letter input)
- ❤️ 6 lives per game
- 🏆 Win/loss detection with the correct word revealed at the end

## 🕹️ How to Play

1. The program randomly selects a secret word.
2. You guess one letter at a time.
3. Correct guesses reveal the letter's position(s) in the word.
4. Incorrect guesses cost you a life and advance the hangman drawing.
5. **Win** by guessing all letters before running out of lives.
6. **Lose** if you reach 6 incorrect guesses — the hangman is complete and the word is revealed.

## 📋 Requirements

- Python 3.x
- No external libraries needed (uses only the built-in `random` module)

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/your-username/CodeAlpha_hangman_game.git
cd CodeAlpha_hangman_game
```

### Run the game
```bash
python CodeAlpha_hangman_game.py
```

## 📁 Project Structure

```
CodeAlpha_hangman_game/
├── CodeAlpha_hangman_game.py   # Main game script
└── README.md                   # Project documentation
```

## 🧠 Word List

The game currently selects from the following words:
```
python, logic, syntax, matrix, kernel
```
Feel free to expand this list in the `words` variable to add more variety!

## 🎨 Sample Gameplay

```
====================================
    WELCOME TO THE HANGMAN GAME!
====================================
Rules: Guess the hidden word letter by letter. You have 6 lives.

           --------
           |      |
           |
           |
           |
           |
        - - - - -

Word to guess: _ _ _ _ _ _
Guessed letters: None
Remaining lives: 6
----------------------------------------
Enter a letter:
```

## 🔮 Future Improvements

- [ ] Add difficulty levels with different word categories
- [ ] Track score/streak across multiple rounds
- [ ] Add a GUI version using Tkinter or Pygame
- [ ] Load word list from an external file for easy customization

## 🙌 Acknowledgements

Developed as part of the **CodeAlpha Python Programming Internship**.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
