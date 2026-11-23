"""
Filename: fibonacciprinter.py
Author: <Al Gburi, Osamah>
Created: <11/17/2026>
Instructor: Burgess
"""

def n_fibonacci():
    numb = int(input("Enter a non-negative, whole number:\n"))
    a = [0, 1]
    q = ""
    for i in range(numb):
        a.append(a[-1] + a[-2])
    print(*a, sep=", ")
    a.sort(reverse=True)
    print(*a, sep=", ")

def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("\nPrint another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()