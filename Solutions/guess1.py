#! /usr/bin/env python3
#just a function to read in numbers
def read_input(order):
    while True:
        try:
            number = int(input(order))
            break
        except ValueError:
            print("This is not a valid number. Please try again")

    return number

#read in first number
number_to_guess = read_input("Please enter the number to be guessed: ")

#read in second number
try_number = read_input("Guess my numnber: ")

#check if guessed number is bigger or smaller than the first number
if number_to_guess < try_number:
    print("My number is smaller.")
elif number_to_guess > try_number:
    print("My number is bigger.")
else:
    print("YES! This is my number")
