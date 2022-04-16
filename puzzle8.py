#!/usr/bin/python3

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

import argparse

from algorithm import Algorithm
from board import Node

def makeFile(filename : str, heuristic : str, initial : list[int], goal : list[int], solution : list) -> None:
    """ Creates a file with the solution.

    Args:
        filename (str): Name of the file to be created.
        solution (list[Node]): List with the solution to the puzzle.

    Returns:
        None.
    """
    # Format filename properly (remove ".txt")
    filename = filename[:-4]
    filename = f"{filename}_{heuristic}_output.txt"

    depth = solution[0]
    totalGen = solution[1]
    sequence = solution[2]
    fnValues = solution[3]

    # Write to file
    with open(filename, 'w') as f:
        # Counter for the formatting
        j = 0
        # Write initial board
        for i in initial:
            j += 1
            f.write(str(i) + ' ')
            if(j == 3):
                f.write('\n')
                j = 0
        f.write('\n')

        # Write goal board
        for i in goal:
            j += 1
            f.write(str(i) + ' ')
            if(j == 3):
                f.write('\n')
                j = 0
        f.write('\n')

        # Write depth
        f.write(str(depth) + '\n')
        # Write total number of generated nodes
        f.write(str(totalGen) + '\n')

        # Write sequence of moves of black tile
        for i in sequence:
            f.write(str(i) + ' ')
        f.write('\n')

        # Write f(n) values
        for i in fnValues:
            f.write(str(i) + ' ')


def main() -> None:
    """ Main function.

    Returns:
        None.
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description='Solve the 8-puzzle problem using A* search.')
    parser.add_argument('filename', help='The txt file containing the initial and goal states.')
    parser.add_argument('heuristic', help='The heuristic to be used. 1 for Manhattan Distance, 2 for Nilsson Sequence Score.')
    cmdline = parser.parse_args()

    # Read input file
    with open(cmdline.filename, 'r') as f:
        input = []
        for line in f:
            line = line.strip().split()
            input = input + line

    # Create initial and goal states
    input = list(map(int, input))
    init, goal = input[:9], input[9:]

    # Find heuristic from command line
    if cmdline.heuristic == '1':
        heuristic = 1
        heur = "h1"
    elif cmdline.heuristic == '2':
        heuristic = 2
        heur = "h2"
    else:
        raise(ValueError('Invalid heuristic.'))

    # Create initial node
    initialNode = Node(init, goal, heuristic)
    # Call algorithm
    aStar = Algorithm(initialNode)

    # Get solution
    solution = aStar.aStarSearch()
    # Make the file
    makeFile(cmdline.filename, heur, init, goal, solution)


if __name__ == '__main__':
    main()
