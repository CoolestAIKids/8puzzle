#!/usr/bin/python3

"""
Object file for the Board class and Node class

Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

class Board:
    """ Board Class
    
    Attributes:
        board (list[int]): List symbolising state of the puzzle.
        goal (list[int]): List symbolising goal state of the puzzle.
    """
    def __init__(self, board : list[int], goal : list[int]) -> None:
        self.board = board
        self.goal = goal

    
    def __str__(self):
        """ Print method

        Returns:
            str : String representation of the board.
        """
        return f"Current State = \n{self.board}\nGoal State = \n{self.goal}\n"


    @staticmethod
    def getRow(index : int) -> int:
        """ Returns the row of the index.
        
        Args:
            index (int): Index of the board.
        
        Returns:
            int : Row of the index.
        """
        return index // 3
    

    @staticmethod
    def getCol(index : int) -> int:
        """ Returns the column of the index.
        
        Args:
            index (int): Index of the board.
        
        Returns:
            int : Column of the index.
        """
        return index % 3


    @staticmethod
    def distance(current : int, goal : int) -> int:
        """ Calculates the expected distance
            from a tile's current position
            to its goal position.
        
        Args:
            current (int): Index of current tile.
            goal (int): Index of goal tile.
        
        Returns:
            int : The expected distance.
        """
        currRow = Board.getRow(current)
        currCol = Board.getCol(current)

        goalRow = Board.getRow(goal)
        goalCol = Board.getCol(goal)

        horDist = abs(goalRow - currRow)
        verDist = abs(currCol - goalCol)

        distance = horDist + verDist

        return distance


    def manhattanDistance(self) -> int:
        """ Calculates the expected Manhattan
            Distance from board to goal.
        
        Returns:
            int : The Manhattan Distance.
        """
        distance = 0
        for index, item in enumerate(self.board):
            if item == 0:
                continue

            distance += self.distance(index, self.goal.index(item))

        return distance


    def nilssonScore(self) -> int:
        """ Calculates the expected Nilsson  
            Sequence Score from board to goal.
        
        Returns:
            int : The Nilsson Sequence Score.
        """
        pn = self.manhattanDistance()
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
            curr = self.board[val]

            if curr == 0: 
                continue

            succ = successors[curr]
            next = self.board[0] if val == 3 else self.board[indices[index + 1]]

            if succ != next:
                sn += 2

        if self.board[4] != self.goal[4]:
            sn += 1

        return pn + 3 * sn


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
        self.heuristic = heuristic

        if heuristic == 1:
            self.hn = self.state.manhattanDistance()
        elif heuristic == 2:
            self.hn = self.state.nilssonScore()
        else:
            raise ValueError("Invalid Heuristic")

        self.pathcost = self.hn + self.depth

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
