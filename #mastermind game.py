#mastermind game

import random

def display_hint(hint):
    print(" ".join(hint))


def main():
    playing = True
    guesses = []
    number = random.choice(range(1000,10000))
    answer = [int(digit) for digit in str(number)]
    hint = ["x"] * len(answer)
    print("Welcome to mastermind")

    while playing: 

        display_hint(hint)
        guess = input("Take your guess: ")
        guesses_uniq = [int(digit) for digit in str(guess)]
        guesses.append(guesses_uniq)

        for char in range(len(answer)):   
            if answer[char] == guesses_uniq[char]:
                hint[char] = guess[char]
            
            elif "x" not in hint:
                    print("You won")
                    break
       
    
            


        if guess == str(number):
            print("you win")
            playing = False
            break



if __name__ == "__main__":
    main()