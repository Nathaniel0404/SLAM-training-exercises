# Exercise 1: State and Sensor Readings
## Part 1: Representing states
The goal of the first part of the exercises is to create the dataclasses that represent the different states we have to consider in our system. We want to create dataclasses for each of the different states we handle as it will make reasoning with the system a lot easier later on.

In `src/slam/models.py`, implement the dataclass definitions of `Pose2D`, `Landmark`, `OdomMsg`, and `PerceptionMsg`.

## Part 2: Updating estimates
Now that we have implemented the different objects we are going to be handling, we can then implement how they interact with each other. 

In `src/slam/estimation.py`, implement the functions that allows us to estimate the new position of the vehicle, and the position of a landmark we have detected. 

Remember that we want our $\theta$ value to be wrapped in $[-\pi,\pi]$. 
(Hint: You may want to consider making a helper function)

## Running tests
Run `python -m pytest tests/test_models.py -v` and `python -m pytest tests/test_models.py -v`.

## Creating tests
To create new test method or file, the name of it has to begin with `test_...` for pytest to detect it.