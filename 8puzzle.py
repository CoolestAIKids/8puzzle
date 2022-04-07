#!/usr/bin/python3

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

import argparse

def expand(expandNode : Node, activeNodes : list[Node], visitedStates : list[list[int]]) -> None:
    """ Creates the current node's children.

    Args:
        expandNode (Node): Node that we want to expand.
        activeNodes (list[int]): List of nodes that are yet to be expanded.
        visitedNodes (list[list[int]]): List of already visited nodes.

    Returns:
        None. Function modifies the activeNodes and the visitedStates lists.
    """
    emptyIndex = expandNode.state.index(0)

    if(emptyIndex == 4):
        newState1 = expandNode.state
        newState1[1], newState1[4] = newState1[4], newState1[1]
        move1 = [1, 4, newState1[4]] # Moves are represented with the old index, the new index, and the item that was moved

        newState2 = expandNode.state
        newState2[3], newState2[4] = newState2[4], newState2[3]
        move2 = [3,4,newState2[4]]

        newState3 = expandNode.state
        newState3[5], newState3[4] = newState3[4], newState3[5]
        move3 = [5, 4, newState3[4]]

        newState4 = expandNode.state
        newState4[7], newState4[4] = newState4[4], newState4[7]
        move4 = [7,4, newState4[4]]

        if (newState1 not in visitedStates):
            newNode1 = Node(newState1, expandNode, expandNode.depth+1, move1)
            activeNodes.append(newNode1)
        if (newState2 not in visitedStates):
            newNode2 = Node(newState2, expandNode, expandNode.depth+1, move2)
            activeNodes.append(newNode2)
        if (newState3 not in visitedStates):
            newNode3 = Node(newState3, expandNode, expandNode.depth+1, move3)
            activeNodes.append(newNode3)
        if (newState4 not in visitedStates):
            newNode4 = Node(newState4, expandNode, expandNode.depth+1, move4)
            activeNodes.append(newNode4)


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
        expand(currentState, activeNodes, visitedStates)


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
