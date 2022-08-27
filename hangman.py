import random

word_list = ["belzebu", "amora", "coxinha", "merendeira", "supino"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess =input("Escolha uma letra").lower()
print(guess)
for letter in chosen_word:
    if letter == guess:
        print("Certo")
    else:
        print("Errado")

display = []
for letter in chosen_word:
    display += "_"
print(display)