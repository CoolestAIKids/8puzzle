#!/usr/bin/python3

import argparse

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""


class Node:
    pass

def manhattanDistance(currentState : list[int], goalState : list[int]) -> int:
    """ Calculates the expected Manhattan Distance 
        from currentState to goalState.
    
    Args:
        currentState (list[int]): List containing the current state.
        goalState (list[int]): List containing the goal state.
    
    Returns:
        int : The Manhattan Distance.
    """
    distance = 0
    for index, item in enumerate(currentState):
        if item == 0:
            continue

        currRow = index//3
        currCol = index%3
        
        goalRow = goalState.index(item)//3
        goalCol = goalState.index(item)%3
        
        horDist = abs(goalRow - currRow)
        verDist = abs(currCol - goalCol)

        distance += horDist + verDist

    return distance


def nillsonScore(currentState: list[int], goalState: list[int]) -> int:
    """ Calculates the expected Nillson Sequence 
        Score from currentState to goalState.
    
    Args:
        currentState (list[int]): List containing the current state.
        goalState (list[int]): List containing the goal state.
    
    Returns:
        int : The Nillson Sequence Score.
    """
    pn = manhattanDistance(currentState, goalState)
    sn = 0
    
    
    
    return pn + 3 * sn


def expand(expandNode : Node, activeNodes : list[Node], visitedStates : list[list[int]]) -> None:
    pass


def aStarSearch(currentState : Node, goalState : list[int]) -> list:
    pass


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
