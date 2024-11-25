#hangman game
import random
class Hangman:

    def __init__(self):
        print("Welcome to hangman the game, we have a random word that is gonna be selected from 20 words")
        
    def main(self):

        words = [\
            "Umbrella", "Galaxy", "Serendipity", "Clockwork", "Zephyr", "Harmony",
            "Kaleidoscope", "Whisper", "Quantum", "Mosaic", "Enigma", "Pensive",
            "Solstice", "Catalyst", "Ethereal", "Labyrinth", "Reverie", "Tranquility",
            "Vortex", "Euphoria"
            ]
        random_word = random.choice(words)
        numb_of_guesses = len(random_word) + 2
        print("_" * len(random_word))
       
Hangman()

