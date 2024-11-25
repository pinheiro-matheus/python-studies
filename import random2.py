import random 


print("Welcome to hangman the game, we have a random word that is gonna be selected from 20 words")
words = [\
            "umbrella", "galaxy", "serendipity", "clockwork", "zephyr", "harmony",
            "kaleidoscope", "whisper", "quantum", "mosaic", "enigma", "pensive",
            "solstice", "catalyst", "ethereal", "labyrinth", "reverie", "tranquility",
            "vortex", "euphoria"
            ]
random_word = random.choice(words)
numb_of_guesses = len(random_word) + 2
word =("_" * len(random_word))
guesses = []
new_word = []
while numb_of_guesses > 0:
    guess = input("Select a characther: ") 
    guesses.append(guess)
    print(guesses)
    print(random_word)
    if guess not in random_word:
        numb_of_guesses -= 1
        for char in random_word:
            if char == guess:
                word.replace("_", guess)
                print(word)
    else:
        new_word.append(guess)
        print(new_word)





