# Collatz Sequence

A small CLI tool that computes and displays the Collatz sequence for a given integer greater than 1.  
It repeatedly transforms the number: if even, divides by 2; if odd, multiplies by 3 and adds 1 — until it reaches 1.

## Features
- Validates input (requires integer > 1)
- Clear step-by-step sequence output
- Robust prompting for correct input

## Requirements
- Python 3.6+

## Usage
```bash
python collatz.py
```

## Next Improvements
- Add command-line argument support (e.g., python collatz.py 6)
- Log the sequence to a file
- Visualize the sequence length or values using a simple plot