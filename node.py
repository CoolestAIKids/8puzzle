#!/usr/bin/python3

"""
Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

from board import Board

class Node:
    """ Node Class

    Attributes:
        board (list[int]): List symbolising state of the puzzle.
        goal (list[int]): List symbolising goal state of the puzzle.
        heuristic (int): The heuristic value of the current node.  
            1 for Manhattan Distance
            2 for Nilsson Sequence Score
        parent (list[int]): Pointer to the parent node. Defaults to None.
        depth (Node): Depth of the current node in the tree. Defaults to 0.
        move (str): The movement of the blank square. One of [U, D, L, R]. Defaults to None.
    """
    def __init__(self, board, goal, heuristic, parent = None, depth = 0, move = None):
        self.state = Board(board, goal)
        self.parent = parent
        self.depth = depth
        self.move = move

        hn = self.state.manhattanDistance() if heuristic == 1 else self.state.nilssonScore()
        self.pathcost = hn + self.depth

    def __eq__(self, other) -> bool:
        """ Checks if two nodes are equal.

        Args:
            other (Node): Node to compare to.

        Returns: 
            bool: True if the nodes are equal, False otherwise.
        """
        if isinstance(other, Node):
            return self.state == other.state
        else:
            return False
