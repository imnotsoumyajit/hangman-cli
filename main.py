import random

# List of words for the game
words = ["python", "hangman", "challenge", "programming", "interactive"]

# Function to select a random word from the list
def get_random_word(word_list):
    return random.choice(word_list).lower()

# Main game function
def play_hangman():
    word = get_random_word(words)
    guessed_word = ["_"] * len(word)  # List to display correctly guessed letters
    guessed_letters = set()  # Set to track letters that have been guessed
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        # Check for valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Update guessed word if letter is correct
        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            print("Good guess:", " ".join(guessed_word))
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        # Check for win condition
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print(f"Out of attempts! The word was '{word}'. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_hangman()
