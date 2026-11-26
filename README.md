
# Conway's Game of Life

Conway's Game of Life is a cellular automaton devised by British mathematician **John Horton Conway** in 1970. It is a zero-player game, meaning its evolution is determined entirely by its initial configuration, with no further user interaction required.

## Overview

The game consists of a two-dimensional grid of cells, where each cell can be in one of two states: **Alive** or **Dead**. Each cell interacts with its eight neighboring cells, and its state changes from one generation to the next according to a set of simple rules.

## Rules

The next state of each cell is determined by the following four rules:

1. **Underpopulation:** A live cell with fewer than two live neighbors dies.
2. **Survival:** A live cell with two or three live neighbors survives.
3. **Overpopulation:** A live cell with more than three live neighbors dies.
4. **Reproduction:** A dead cell with exactly three live neighbors becomes alive.

## How It Works

The simulation begins with an initial arrangement of live and dead cells. With each generation, all cells update their states simultaneously based on the rules above.

These simple interactions can produce fascinating patterns, including stable structures, oscillators, and moving patterns called spaceships.

## Objective

There is no specific winning or losing condition. The purpose is to explore how complex and unpredictable patterns can emerge from a small set of simple mathematical rules.

Conway's Game of Life demonstrates how simple interactions can lead to surprisingly complex behavior.
