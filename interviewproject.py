"""
Filename: interview.py
Author: <Al Gburi, Osamah>
Created: <08/25/2026>
Instructor: Burgess
"""
import time

score: int = 0

print("Welcome! I am interview bot! Please answer the following questions.\nMake sure to answer yes or no questions with 'yes', 'y' or 'no', 'n'.\n")
time.sleep(1)

age = input("How old are you? \n")
if int(age) < 18: print("\nYou should still be in school.")
elif int(age) > 18: print("\nYou are old.")

time.sleep(1)

degree = input("\nDo you have a degree? \n")
if degree == "yes" or degree == "y":
    print("\nThat is good.")
    score: int =+ 1
elif degree == "no" or degree == "n":
    print("\nGo get one.")
    score: int =- 1

job = input("\nWhat do you want to teach? \n")

print("\nOkay.")

time.sleep(1)

taught = input("\nHave you ever taught before? \n")
if taught == "yes" or taught == "y":
    print("\nThat is good.")
    score: int =+ 1
elif taught == "no" or taught == "n":
    print("\nThat is bad.")
    score: int =- 1

time.sleep(1)


like = input("\nDo you like students? \n")
if like == "yes" or like == "y":
    print("\nThat is great to hear.")
    score: int =+ 2
elif like == "no" or like == "n":
    print("\nThat is horrible.")
    score: int =- 2

time.sleep(1)

print("\nProcessing answers. Please wait for a few moments.")

lp: int = 5

while lp > 0:
    time.sleep(0.5)
    print(".")
    lp -= 1

print("Finished.")

time.sleep(1)

if score == 2:
    print("\nWe'll give you a chance.")
elif score >= 3:
    print("\nYou are hired!")
elif score < 2:
    print("\nYou are bad! Don't come back!")


print("\nThese are your answers.")
time.sleep(1)
print("age: ",age)
print("degree: ",degree)
print("teach: ",job)
print("taught before: ",taught)
print("like students: ",like)
time.sleep(1)
print("\nThis was your interview score: ", score)