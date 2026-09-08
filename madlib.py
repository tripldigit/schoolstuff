"""
Filename: madlib.py
Author: <Al Gburi, Osamah>
Created: <08/31/2026>
Instructor: Burgess
"""


import time
from xml import dom

print("Please answer all prompts. I will then create a story with your answers.")

time.sleep(1.5)

name = input("Enter character's name: ")
time.sleep(0.5)
adj1 = input("Enter an adjective: ")
time.sleep(0.5)
obj = input("Enter an object: ")
time.sleep(0.5)
rare = input("Enter a rarity: ")
time.sleep(0.5)
pro1 = input("Enter a pronoun (he,her,etc): ")
time.sleep(0.5)
adj2 = input("Enter an adjective: ")
time.sleep(0.5)
occ = input("Enter an occupation: ")
time.sleep(0.5)
pro2 = input("Enter a pronoun (he,her,etc): ")
time.sleep(0.5)
num = input("Enter a number: ")
time.sleep(0.5)
ti = input("Enter a unit of time: ")
time.sleep(0.5)
sound = input("Enter a sound: ")
time.sleep(0.5)
direction = input("Enter a direction: ")
time.sleep(0.5)
color = input("Enter a color: ")
time.sleep(0.5)
creature = input("Enter a creature (real or fictional): ")
time.sleep(0.5)
verb = input("Enter a verb: ")
time.sleep(0.5)
adj3 = input("Enter an adjective: ")
time.sleep(0.5)
size = input("Enter a size: ")
time.sleep(0.5)
verb2 = input("Enter a verb: ")
time.sleep(0.5)
adj4 = input("Enter an adjective: ")
time.sleep(0.5)
group = input("Enter a group: ")
time.sleep(0.5)

print("Processing answers...")
time.sleep(0.5)
lp: int = 10
while lp > 0:
    time.sleep(0.5)
    print(".")
    lp -= 1

print("Finished. \n Here is the story.")
time.sleep(1.5)
print(f"\n{name} walked through the woods, looking for the {adj1} {obj}.")
time.sleep(2.5)
print(f"It was pretty {rare}. If {pro1} could just find it, they would be the {adj2} {occ} ever!")
time.sleep(2.5)
print(f"That’s if {pro2} ever finds it. They’ve been searching for {num} {ti}!")
time.sleep(2.5)
print(f"Suddenly {name} heard a noise.")
time.sleep(2.5)
print(f"A {sound} from their {direction}.")
time.sleep(2.5)
print(f"And, from there, a {color} {creature} {verb} toward {pro2}!")
time.sleep(2.5)
print(f"But, wait, they have the {obj}! It looks so {adj3}, and surprisingly {size}.")
time.sleep(2.5)
print(f"{name} {verb2} around, scaring off the {creature}.")
time.sleep(2.5)
print(f"Then, they grabbed the {obj}, holding it high up in the air. Now, time to show it off to the {adj4} {group}!")
time.sleep(2.5)

print("\nI hope you enjoyed that story.")