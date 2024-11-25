#number guessing machine

import random
import time

def game():
    count = 0
    print("Welcome to guessing macinhe")
    time.sleep(0.2)
    print("First you have to select a range")
    time.sleep(0.2)
    user_range = input("Chosse 2 numbers, this will be the starter number and the end number for our range, ex:1, 100: ")
    range_ = list(user_range)
    print("The range is: %s" %str((range_))) 
    right_numb = random.randint(user_range)
    time.sleep(0.2)
    guess = int(input("Now, Try guessing the number: "))
    while count < 3:
        if guess < right_numb:
            print(" Guess Higher")
        elif guess > right_numb:
            print("Go lower")
        elif guess == right_numb:
            print("You got it right")

game()