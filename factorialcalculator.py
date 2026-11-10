"""
Filename: factorialcalculator.py
Author: <Al Gburi, Osamah>
Created: <11/10/2026>
Instructor: Burgess
"""

def factorial():
    numb = int(input("Enter a non-negative, whole number: "))
    answer = 1
    if numb == 0:
        print("0! = 1")
    else:
        for i in range(1, numb + 1):
            answer *= i
        print(f"{numb}! =", answer)


def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")


if __name__ == "__main__":
    main()