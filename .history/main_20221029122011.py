import random

word_list = ["aardvark", "baboon", "camel"]
selected_word = random.choice(word_list)
array_selected_word = ([*selected_word])


user_input = input("Select a letter").lower()

display = []

for letter in range(len(selected_word)):
    display += "_"

for pos in range(len(selected_word)):
    letter = selected_word[pos]
    if user_input == letter:
        display[pos] = letter
    else:
        display[pos] = '_'
print(display)
