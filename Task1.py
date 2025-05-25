import random

# Predefined list of words
words = ["apple", "house", "water", "pizza", "chair"]

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")

# Game loop
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

# Result
if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)

