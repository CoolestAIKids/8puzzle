#!/usr/bin/python3

"""
Object file for the Board class

Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

from today import manhattanDistance


class Board:
    """ Board Class
    
    Attributes:
        board (list[int]): List symbolising state of the puzzle.
        goal (list[int]): List symbolising goal state of the puzzle.
    """
    def __init__(self, board : list[int], goal : list[int]) -> None:
        self.board = board
        self.goal = goal


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
        currRow = current//3
        currCol = current%3
        
        goalRow = goal//3
        goalCol = goal%3

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
        pn = self.manhattanDistance(self.board, self.goal)
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


    def pathCost(self, depth : int, heuristic : int) -> int:
        """ Calculates the path cost f(n)

        Args:
            depth (int): Depth of the node.
            heuristic (int): Heuristic value of the node. 
                1 for Manhattan Distance
                2 for Nilsson Sequence Score

        Returns:
            int : The path cost f(n).
        """
        hn = self.manhattanDistance() if heuristic == 1 else self.nilssonScore()

        return depth + hn
