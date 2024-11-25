#number guessing
import random

def guessing_machine():
    count = 0
    user_input1 = input("Chose a a range, fist number:")
    user_input2 = input("Second number: ")
    user_input3 = int(input("Guess a number: "))
    random_numb = random.randint(int(user_input1), int(user_input2))
    while count < 3:
        if user_input3 != random_numb:
            count += 1
            print("Wrong number")
            if user_input3 < random_numb:
                print("TRy go higher")
                count += 1
                user_input3 = int(input("Guess number 2: "))

            elif user_input3 > random_numb:
                print("Try go lower")
                count += 1
                user_input3 = int(input("Guess number 2: "))
            else: 
                print("Better luck next time")
        else: 
            print("You got it rigth")
            break

            

    

guessing_machine()


  