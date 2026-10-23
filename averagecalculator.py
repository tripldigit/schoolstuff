"""
Filename: averagecalculator.py
Author: <Al Gburi, Osamah>
Created: <10/23/2026>
Instructor: Burgess
"""

print("Welcome to the average calculator.\nIf inputting a fraction, please use it's decimal form instead.\ni.e. 0.5 instead of 1/2")

yes = 1

tot = 0

nums = []

while yes == 1:
    nums.append(float(input("Enter a number: ")))
    tot += 1
    wow = sum(nums)
    print(f"The current sum is {wow}.")
    print(f"The total amount of numbers added is {tot}.")
    avg = wow/tot
    print(f"The average is {avg}.")
    question = input("Would you like to continue? (y/n): ")
    if question == "y":
        yes = 1
    else:
        yes = 0
