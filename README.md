# DFS Maze Solver 

This project solves a 2D maze with the help of DFS algorithm. It takes an input file containing the maze in ASCII format, convert it to Adjacency List and solve the maze. 
It also implements its own Graph data structure to help with the maze represantation

## Installation 

The package does not have any dependencies besides Python itself.

```bash
pip install requirements.txt
```

## Usage

The solve_ program is a command-line interface for solving mazes. You must use the -f or --file and the path to input file, to use it. For example: 

```bash
python solve_maze.py -f data/input_maze.txt
```
I have also added an extra mode where you can choose to draw the path at the output. Just use -s yes or --show yes. For example: 

```bash
python solve_maze.py -f data/input_maze.txt -s yes
```

To run demo1_maze.py and demo2_maze.py use the following 

```bash
python demo1_maze.py
```

```bash
python demo2_maze.py
```