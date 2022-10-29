import random

word_list = ["aardvark", "baboon", "camel"]
selected_word = random.choice(word_list)
array_selected_word = ([*selected_word])

print(array_selected_word)

user_input = input("Select a letter").lower()

for letter in array_selected_word:
    if user_input == letter:
        print("Correct")
    else:
        print("Incorrect")

display = []

for letter in range(array_selected_word):
    if user_input == letter:
        display += letter
print(display)
