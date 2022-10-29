from array import array
import random

hangmen = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
selected_word = random.choice(word_list)
array_selected_word = ([*selected_word])

game_end = False
display = []
lives = 6

print(display)

for _ in range(len(selected_word)):
    display += "_"

while not game_end:
    user_input = input("Select a letter: ").lower()

    if user_input in display:
        print(f"\nYou've already used this letter. Please try another letter.")

    for pos in range(len(selected_word)):
        letter = selected_word[pos]
        if user_input == letter:
            display[pos] = letter

    if user_input != '':
        print(display)

    print(hangmen[lives])

    if user_input not in array_selected_word:
        print(
            f"{user_input} is not in the word. You only have {lives} lives remaining. \n")
        lives -= 1
        if lives == 0:
            game_end = True
            print("You've lost all of your lives.")
    if display == array_selected_word:
        print("You won!")
        game_end = True
