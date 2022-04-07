#!/usr/bin/python3

import argparse

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
""" Description
    
    Args:
        arg1 (type): Description.
        arg2 (type): Description.
    
    Returns:
        type : Description.
"""

class Node:
    """ Node Class

    Attributes:
        state: List symbolising state of the puzzle.
        parent: Pointer to the parent node.
        depth: Depth of the current node in the tree.
        move: The movement of the blank square. One of [U, D, L, R]
    """
    def __init__(self, state, parent, depth, move = None):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.move = move


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


def nilssonScore(currentState: list[int], goalState: list[int]) -> int:
    """ Calculates the expected Nilsson Sequence 
        Score from currentState to goalState.
    
    Args:
        currentState (list[int]): List containing the current state.
        goalState (list[int]): List containing the goal state.
    
    Returns:
        int : The Nilsson Sequence Score.
    """
    pn = manhattanDistance(currentState, goalState)
    sn = 0
    
    successors = {
        1 : 2,
        2 : 3,
        3 : 4,
        4 : 5,
        5 : 6,
        6 : 7,
        7 : 8,
        8 : 1
    }
    indices = [0, 1, 2, 5, 8, 7, 6, 3]
    for index, val in enumerate(indices):
        curr = currentState[val]

        if curr == 0: 
            continue
        
        succ = successors[curr]
        next = currentState[0] if val == 3 else currentState[indices[index + 1]]

        if succ != next:
            sn += 2

    if currentState[4] != goalState[4]:
        sn += 1
    
    return pn + 3 * sn


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
