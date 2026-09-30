"""
Filename: triviagame.py
Author: <Al Gburi, Osamah>
Created: <09/30/2026>
Instructor: Burgess
"""

correct = 0
score = 0

print("Hello, welcome to this Trivia!\nThis Trivia will be about...\nMinecraft!")
print("Please answer with one word, all lower-case. Do not use 'the'")
print("Example:\n'nether' not 'The Nether'")


q1 = input("\nWhat is the most abundant block in Minecraft?")
if q1 == "netherrack":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q1 != "netherrack":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q2 = input("\nWhere is the most abundant block in Minecraft located?")
if q2 == "nether":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q2 != "nether":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q3 = input("\nWho do you TRADE with in Minecraft (not barter)?")
if q3 == "villager":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q3 != "villager":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q4 = input("\nWho do you BARTER with in Minecraft?")
if q4 == "piglin":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q4 != "piglin":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q5 = input("\nWhere are they located in Minecraft?")
if q5 == "bastion":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q5 != "bastion":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q6 = input("\nWhat is the new dimension being added to Minecraft?")
if q6 == "sift":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q6 != "sift":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q7 = input("\nWhat other dimension has not been mentioned, in answers, aside from the Overworld?")
if q7 == "end":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q7 != "end":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q8 = input("\nWhat is the boss, with three heads, in Minecraft?")
if q8 == "wither":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q8 != "wither":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q9 = input("\nWhat is the strongest material for making weapons and armor in Minecraft?")
if q9 == "netherite":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q9 != "netherite":
    if score > 0:
        score = score - 1
    print("Incorrect.")

q10 = input("\nLastly, who made Minecraft?")
if q8 == "notch":
    correct = correct + 1
    score = score + 2
    print("Correct!")
elif q10 != "notch":
    if score > 0:
        score = score - 1
    print("Incorrect.")

print("Your score is:", score)
print("You got", correct, "questions right out of 10")