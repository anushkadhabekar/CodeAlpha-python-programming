import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_incorrect = 6
incorrect_guesses = 0

# Display blanks for the word
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display:

    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!\n")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

# Game result
if "_" not in display:
    print("🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("💀 Game Over!")
    print("The word was:", word)