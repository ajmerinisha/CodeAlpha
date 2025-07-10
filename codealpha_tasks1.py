import random

word_list = ['apple', 'banana', 'cherry', 'grape', 'orange']

word_to_guess = random.choice(word_list)
guessed_word = ['_'] * len(word_to_guess)
guessed_letters = []
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(" ".join(guessed_word))

while attempts < max_attempts and '_' in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good guess! '{guess}' is in the word.")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts += 1

    print(" ".join(guessed_word))
    print(f"Attempts left: {max_attempts - attempts}")


if '_' not in guessed_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Out of attempts! The word was:", word_to_guess)
