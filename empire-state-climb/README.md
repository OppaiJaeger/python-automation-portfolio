# Empire State Building Climb Simulation

This program simulates 500 random walks, representing attempts to climb the Empire State Building under specific probabilistic rules. The simulation determines the probability of a person reaching or exceeding a height of 60 floors after 100 steps.

## Features
- Simulates a random walk: Each of the 500 walks consists of 100 steps with probabilistic movements.
- Visualizes results: A histogram displays the distribution of the final floor reached.
- Calculates odds: The code computes and prints the probability of reaching at least floor 60.

## Rules of the Random Walk

- A roll of 1 or 2 on a six-sided die moves you down one floor (minimum floor is 0).
- A roll of 3, 4, or 5 moves you up one floor.
- A roll of 6 moves you up a random number of floors (1-6).
- There is a 0.1% chance at each step to fall back to floor 0.

## File Structure

```text

empire-state-climb/
├── climb_simulation.py  # Main Python program
└── README.md # Project documentation

```

## Usage

To run the simulation and calculate the odds:

```bash
python climb_simulation.py
```
