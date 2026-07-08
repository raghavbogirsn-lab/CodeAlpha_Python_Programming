import random

def play_hangman():
    # 1. Predefined list of exactly 5 words (Scope constraint)
    words = ["python", "logic", "syntax", "matrix", "kernel"]
    
    # Randomly select the secret word
    secret_word = random.choice(words)
    
    # Use a set to track guessed letters for optimized tracking
    guessed_letters = set()
    
    # Set the limit of incorrect guesses to exactly 6
    max_attempts = 6
    incorrect_guesses = 0

    # Advanced Touch: Visual ASCII stages for the console
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
        - - - - -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
        - - - - -
        """
    ]

    print("====================================")
    print("    WELCOME TO THE HANGMAN GAME!    ")
    print("====================================")
    print(f"Rules: Guess the hidden word letter by letter. You have {max_attempts} lives.")

    # Main game loop
    while incorrect_guesses < max_attempts:
        # Display current hangman visual state
        print(stages[incorrect_guesses])
        
        # Build and display the hidden word progress (e.g., p _ t h _ n)
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        print(f"Word to guess: {' '.join(display_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining lives: {max_attempts - incorrect_guesses}")
        print("-" * 40)

        # Check if the player won (no blanks left)
        if "_" not in display_word:
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: '{secret_word.upper()}'!")
            break

        # Advanced Input Validation Loop
        while True:
            guess = input("Enter a letter: ").lower().strip()
            
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Invalid input! Please enter a single alphabetical letter.")
            elif guess in guessed_letters:
                print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            else:
                break  # Input is verified and clean
        
        # Log the guess
        guessed_letters.add(guess)

        # Evaluate the guess using conditional logic
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses += 1

    # Main loop termination check (Loss state)
    if incorrect_guesses == max_attempts:
        print(stages[incorrect_guesses])
        print("💀 GAME OVER! You ran out of attempts.")
        print(f"The correct word was: '{secret_word.upper()}'")

if __name__ == "__main__":
    play_hangman()