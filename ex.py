#mastermid


import random


def display_hint(hint):
    print(" ".join(hint))

def main():
    playing = True
    guesses = []
    number = random.choice(range(1000, 10000))
    answer = [int(digit) for digit in str(number)]
    hint = ["x"] * len(answer)
    print("Welcome to Mastermind! Try to guess the 4-digit number.")

    while playing: 
        display_hint(hint)
        guess = input("Take your guess: ")
        
        if len(guess) != len(answer) or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        guesses_uniq = [int(digit) for digit in guess]
        guesses.append(guesses_uniq)

        if guesses_uniq == answer:
            print("You win! The number was:", number)
            playing = False
            break
        
        # Check for correct digits and their positions
        for char in range(len(answer)):
            if answer[char] == guesses_uniq[char]:
                hint[char] = guess[char]
        
        if "x" not in hint:
            print("You won! The number was:", number)
            playing = False
        
        print("Your previous guesses:", guesses)

if __name__ == "__main__":
    main()
    