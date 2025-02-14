# GameOfLife_Pygame

A simple implementation of Conway's Game of Life in Python using Pygame for visualization.

## Installation

### Clone the repository  
```bash
git clone https://github.com/Karlingas/GameOfLife_Pygame.git
cd GameOfLife_Pygame
```
### Install dependencies
```bash
pip install pygame
```
### Run the simulation
```bash
python game_of_life.py
```

## Controls

Left-click on a cell to toggle its state.
Click the "PAUSE" button to pause or resume the simulation.
Resize the window to expand or contract the grid without losing its state.

In the code, you can modify the tick parameter to alter the generations per second. Right now is set to 15 which i think is good enough to see the evolution of the cells but not be caotic.

## About Conway’s Game of Life

The Game of Life is a zero-player game where cells evolve based on 4 simple rules:

-Any live cell with fewer than 2 neighbors dies as of starvation

-Any live cell with more than 3 neighbors dies as of overpopulation.

-Any live cell with 2 or 3 neighbors will keep living.

-Any dead cell with exactly 3 live neighbors becomes alive.

A neighbor is defined as an adjacent cell, so a cell can have a maximun of 8 neighbors.

## Screenshots

![Game of Life Screenshot](/media/GOL_Screenshot.png)
