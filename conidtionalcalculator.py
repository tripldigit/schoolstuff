"""
Filename: conditionalcalculator.py
Author: <Al Gburi, Osamah>
Created: <09/10/2026>
Instructor: Burgess
"""

import time

print("Hello, welcome to the Five-Function Calculator.")
time.sleep(1.5)
print("Shortly, you will be prompted to enter a number.")
time.sleep(1.5)
print("Please do not enter fractions. Use their decimal forms instead.")
time.sleep(1.5)
print("Example:\n '0.5' instead of '1/2'")
time.sleep(1.5)
print("Make sure to enter it in digits also, not written words.")
time.sleep(1.5)
print("Example:\n   '3' is correct.\n   'Three' is incorrect.")
time.sleep(1.5)

n1 = float(input("Please enter a number: "))
time.sleep(1.5)

print("Now, please enter your choice of operation. Follow the input guidelines.")
time.sleep(1)
print("For Addition: '+'")
time.sleep(0.85)
print("For Subtraction: '-'")
time.sleep(0.85)
print("For Multiplication: '*'")
time.sleep(0.85)
print("For Division: '/'")
time.sleep(0.85)
print("For Exponential: '^'")
time.sleep(0.85)
OP = input("Please enter your choice: ")
time.sleep(1.5)

n2 = float(input("Please enter a second number. Follow the pre-established format: "))
time.sleep(1.5)

print("Processing")
time.sleep(0.35)
lp: int = 5
while lp > 0:
    time.sleep(0.5)
    print(".")
    lp -= 1
print("Done.")
time.sleep(1.5)

if OP == "+":
    print(f"Addition:\n{n1} + {n2} =", n1 + n2)
elif OP == "-":
    print(f"Subtraction:\n{n1} - {n2} =", n1 - n2)
elif OP == "*":
    print(f"Multiplication:\n{n1} * {n2} =", n1 * n2)
elif OP == "/":
    print(f"Division:\n{n1} / {n2} =", n1 / n2)
elif OP == "^":
    print(f"Exponential:\n{n1}^{n2} =", n1 ** n2)
time.sleep(1.5)

print("Thank you for using the Five-Function Calculator.")