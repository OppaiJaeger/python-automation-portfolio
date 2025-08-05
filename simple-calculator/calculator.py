"""Simple Calculator: modular implementation with validation and logging."""

import datetime
import os

LOGFILE = "history.txt"
OPERATORS = ["+", "-", "*", "/"]

def get_number(prompt):
    """Prompt until a valid float is entered and return it."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Please try again.")

def get_operator():
    """Prompt until a valid operator is entered and return it."""
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in OPERATORS:
            return op
        print("Invalid operator. Choose one of +, -, *, /.")

def perform_calculation(a, b, operator):
    """Perform the arithmetic and handle division by zero."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            print("Error: Division by zero.")
            return None
        return round(a / b, 4)

def log_calculation(a, b, operator, result):
    """Append a successful calculation to the log file."""
    is_new = not os.path.exists(LOGFILE) or os.path.getsize(LOGFILE) == 0
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOGFILE, "a", encoding="utf8") as f:
        if is_new:
            f.write("# Simple Calculator History Log\n")
        f.write(f"{timestamp} | {a} {operator} {b} = {result}\n")

def ask_continue():
    """Ask whether to continue; return True to continue."""
    while True:
        answer = input("Do another calculation? (y/n): ").strip().lower()
        if answer.startswith("y"):
            return True
        if answer.startswith("n"):
            return False
        print("Please answer y or n.")

def main():
    print("Welcome to the Simple Calculator!")
    while True:
        num1 = get_number("Enter the first number: ")
        operator = get_operator()
        num2 = get_number("Enter the second number: ")

        result = perform_calculation(num1, num2, operator)
        if result is None:
            continue  # e.g., division by zero
        print(f"The result of {num1} {operator} {num2} is: {result}")

        log_calculation(num1, num2, operator, result)
        print("Logged calculation.")

        if not ask_continue():
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
