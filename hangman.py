import random


words = ["apple", "banna", "kiwi", "grape", "mango", "passion fruit", "strawberry", "avacado", "watermellon"]
random_word = random.choice(words)
numb_guesses = len(random_word) + 2
word_cryp = "_" * len(random_word)
word_uncryp = []
print("apresentation")
guess = input("guess: ")
guesses = []
while numb_guesses > 0:
    print(word_cryp)
    if guess in random_word:
        numb_guesses -= 1

        
    else:
        numb_guesses -= 1
   
    
    

