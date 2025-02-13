# GameOfLife_Pygame

A simple implementation of Conway's Game of Life in Python using Pygame for visualization.

## Features

Live Simulation: Watch the cellular automaton evolve in real time.
Pause & Resume: Control the simulation with a button.
Interactive Editing: Click on cells to toggle their state (alive/dead).
Resizable Window: The grid adapts dynamically when resizing the window, keeping the previous state.
## Installation

## Clone the repository  
```bash
git clone https://github.com/Karlingas/GameOfLife_Pygame.git
cd GameOfLife_Pygame
```
Install dependencies
```bash
pip install pygame
```
Run the simulation
```bash
python game_of_life.py
```

## Controls

Left-click on a cell to toggle its state.
Click the "PAUSE" button to pause or resume the simulation.
Resize the window to expand or contract the grid without losing its state.
About Conway’s Game of Life

The Game of Life is a zero-player game where cells evolve based on simple rules:

Any live cell with fewer than 2 or more than 3 neighbors dies.
Any dead cell with exactly 3 live neighbors becomes alive.
This leads to complex and interesting emergent patterns!

## Screenshots

![Game of Life Screenshot](/media/GOL_Screenshot.png)
