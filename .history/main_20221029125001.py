from array import array
import random

word_list = ["aardvark", "baboon", "camel"]
selected_word = random.choice(word_list)
array_selected_word = ([*selected_word])

game_end = False
display = []
lives = 5

print(display == array_selected_word)

for _ in range(len(selected_word)):
    display += "_"

while not game_end:
    user_input = input("Select a letter").lower()

    for pos in range(len(selected_word)):
        letter = selected_word[pos]
        if user_input == letter:
            display[pos] = letter
    print(display)

    if user_input not in array_selected_word:
        lives -= 1
    if display == array_selected_word:
        print("You won!")
        game_end = True
