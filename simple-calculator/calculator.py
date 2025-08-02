"""Simple Calculator: supports +, -, *, / with input validation and rounding."""

import datetime
import os, sys

LOGFILE = "history.txt"

def log_calculation(a, b, operator, result):
    """Append a successful calculation to history.txt with timestamp."""
    # Ensure logfile has header if newly created (optional)
    is_new = not os.path.exists(LOGFILE) or os.path.getsize(LOGFILE) == 0
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    line = f"{timestamp} | {a} {operator} {b} = {result}\n"
    with open(LOGFILE, "a") as f:
        if is_new:
            f.write("# Simple Calculator History Log\n")
        f.write(line)
result = 0
again = 'y'

print("Welcome to the Simple Calculator!")

while again == 'y':
    # Get first number with validation
    try:
        num1 = float(input("\nEnter the first number: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        continue

    # Get second number with validation
    try:
        num2 = float(input("\nEnter the second number: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        continue

    # Get operator
    operator = input("\nEnter the operation (+, -, *, /): ").strip()
    if operator not in ["+", "-", "*", "/"]:
        print("\nInvalid operator. Please enter one of +, -, *, /.")
        continue

    # Perform calculation with clear handling
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
            continue
        result = round(num1 / num2, 4)

    print(f"\nThe result of {num1} {operator} {num2} is: {result}")

    # Only log if result is numeric (i.e., not an error message)
    try:
        # convert to float to be safe; if result is not numeric this will fail
        numeric_result = float(result)
        log_calculation(num1, num2, operator, numeric_result)
        print("\nLogged calculation.")
    except (ValueError, TypeError):
        # skip logging non-numeric errors
        pass

    again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
    if again.startswith('y'):
        continue  # continue outer calculation loop
    if again.startswith('n'):
        print("\nGoodbye!")
        sys.exit()  # or break out of outer loop if structured that way
    else:
        print("Please answer with yes or no (y/n).")