"""
Filename: simplecalculator.py
Author: <Al Gburi, Osamah>
Created: <09/08/2026>
Instructor: Burgess
"""

import time

print("Hello, welcome to Simple Calculator.")
time.sleep(1.5)
print("Shortly, you will be prompted to enter numbers.\n    Please enter them in digits, not written words.")
time.sleep(1.5)
print("Example:\n   '3' is correct.\n   'Three' is incorrect.")
time.sleep(1.5)
n1 = input("Please enter a number: ")
time.sleep(1.5)
n2 = input("Please enter another number: ")
time.sleep(1.5)

print("Addition:")
print(f"{n1} + {n2} =", float(n1) + float(n2))
time.sleep(1.5)
print("Subtraction:")
print(f"{n1} - {n2} =", float(n1) - float(n2))
time.sleep(1.5)
print("Multiplication:")
print(f"{n1} * {n2} =", float(n1) * float(n2))
time.sleep(1.5)
print("Division:")
print(f"{n1} / {n2} =", float(n1) / float(n2))
time.sleep(1.5)
print("Thank you for using Simple Calculator.")