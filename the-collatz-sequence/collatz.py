"""Collatz sequence: repeatedly transform a number until it reaches 1."""

import sys

def collatz(n):
    """Return the next number in the Collatz sequence."""
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def get_starting_number():
    """Prompt the user for an integer greater than 1."""
    while True:
        try:
            value = int(input("Enter an integer greater than 1: ").strip())
            if value > 1:
                return value
            print("Number must be greater than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Welcome to the Collatz sequence!")
    number = get_starting_number()

    while number != 1:
        number = collatz(number)
        print(number)

if __name__ == "__main__":
    main()
