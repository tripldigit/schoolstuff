"""
Filename: numberguessinggame.py
Author: <Al Gburi, Osamah>
Created: <10/29/2026>
Instructor: Burgess
"""

import random

print("Welcome to the number guessing game!")
print("Shortly, I will generate a random number between 1 and 100.")
print("We will keep going until you get it right!")

rando = random.randint(1, 100)
guess = 0
guesses = 0

while guess != rando:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if guess == rando:
        print("You guessed right!")
        print("Total attempts:", guesses)
    if guess > rando:
        print("Too high!")
    if guess < rando:
        print("Too low!")