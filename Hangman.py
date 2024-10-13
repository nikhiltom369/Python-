import random

# List of words
word_list = ["hey", "hello", "love"]

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)

# Shuffle the letters of the chosen word
shuffled_word = ''.join(random.sample(chosen_word, len(chosen_word)))

# Display the shuffled word as a clue
print(f"Shuffled word (as clue): {shuffled_word}")

# Create a display to hold underscores representing unguessed letters
display = ["_"] * len(chosen_word)
print(" ".join(display))  # Join the display list with spaces between underscores

# Initialize the game status
gameover = False
lives = 6  # Number of incorrect attempts allowed

# Game loop
while not gameover:
    # Get user's guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Update the display with the guessed letter in the correct positions
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        # If the guessed letter is not in the word, reduce the number of lives
        lives -= 1
        print(f"Wrong guess! You have {lives} lives remaining.")
    
    # Show the updated display
    print(" ".join(display))
    
    # Check for game end conditions
    if "_" not in display:
        gameover = True
        print("You win!")
    elif lives == 0:
        gameover = True
        print(f"Game over! The word was: {chosen_word}")
