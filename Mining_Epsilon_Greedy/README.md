# Epsilon Greedy Algorithm: Stardew Valley Mining

## Setup

Before running the scheduler, make sure you have the following installed:

- Python 3.x
- Matplotlib
- Numpy

After installing and setting up python, you can install the needed libraries using pip:
```bash
$ pip install matplotlib numpy
```
[Download python](https://www.python.org/downloads)

[Matplotlib Docs](https://matplotlib.org/stable/users/installing/index.html)

[Numpy Docs](https://numpy.org/install/)


## How to run
Run `python mining.py` in either your terminal or IDE.  The graphs for each simulation
will be displayed to the screen. Some example simulations can be found in the `/imgs` folder.


## Background
We want to find the optimal approach for mining in the Stardew Valley mine. To perform this experiment, we needed the
distributions of stone type in the levels of the mine. The distributions are as follows:

| Level Range | Copper | Iron  | Gold |
|-------------|--------|-------|------|
| 1-19        | 1.0    | 0.0   | 0.0  |
| 21-39       | 0.9    | 0.1   | 0.0  |
| 41-59       | 0.25   | 0.75  | 0.0  |
| 61-79       | 0.225  | 0.675 | 0.1  |
| 81-119      | 0.0625 | 0.1875| 0.75 |


## Code Structure

The code structure is as follows:

**get_probabilites()**: This function calulates the probabilities of finding rocks at different levels
in the mine based on the provided rock distribution.

**choose_action(actions, epsilon)**: This function implements the epsilon-greedy action selection strategy, where it
randomly chooses exploration or exploitation based on the epsilon value.

**run_epsilon_greedy(epsilon, numOfSteps, probabilities, num_simulations)**: This function executes the epsilon-greedy algorithm for a specified number
of time steps and simulations, updating the cumulative rewards and averaging them over simulations.

