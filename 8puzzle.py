#!/usr/bin/python3

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

import argparse
from Algorithm import *
def aStarSearch(currentState : Node, goalState : list[int]) -> list:
    """ Takes initial and goal states calculates the 
        shortest path to the goal state

    Args:
        currentState: Starting node for the algorithm.
        goalState: List containing the goal state.

    Returns:
        A list with the shortest path from the initial state to goal state.
    """
    currentState.heuristic = manhattanDistance(currentState.state, goalState)
    activeNodes = [] #list of the nodes of the tree that could be expanded
    visitedStates = [] #list of states that 

    activeNodes.append(currentState)

    while(len(activeNodes) != 0):
        currentState = activeNodes.pop
        #expand(currentState, activeNodes, visitedStates)


def main() -> None:
    """ Main function.

    Returns:
        None.
    """
    parser = argparse.ArgumentParser(description='Solve the 8-puzzle problem using A* search')
    parser.add_argument('filename', help='The txt file containing the initial and goal states')
    cmdline = parser.parse_args()

    with open(cmdline.filename, 'r') as f:
        input = []
        for line in f:
            line = line.strip().split()
            input = input + line

    input = list(map(int, input))
    init, goal = input[:9], input[9:]
    print(f"{init=}\n{goal=}") # ! Just for initial debugging TODO: Delete


if __name__ == '__main__':
    main()
