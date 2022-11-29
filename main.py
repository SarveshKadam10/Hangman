import random
from replit import clear

from hangman_words import word_list
from hangman_art import stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = len(stages) - 1

from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()


    if guess in display:
      print(display)
      print(f'{guess} is entered already')

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"'{guess} it's not in the word'")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])