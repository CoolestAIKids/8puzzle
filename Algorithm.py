#!/usr/bin/python3

from node import Node
from board import Board
distance = Board.distance


""" Algorithm Class

    Attributes:
        active (list[Node]): List with the current states of the puzzle to be expanded
        visited (list[Node]) : List with the Nodes that were visited already
        totalNodes(Int) : total amount of nodes generated by the algorithm
    """
class Algorithm:
    def __init__(self, initialNode):
        self.active = []
        self.insertActive(initialNode)
        self.visited = []
        self.totalNodes = 1

    def insertActive(self, stateNode : Node) -> None:
        """ Properly inserts a node in the list of active nodes.

                Args:
                    stateNode (Node): Node that we want to insert into active

                Returns:
                    None. Function modifies the activeNodes and the visitedStates lists.
                """
        self.active.append(stateNode)
        if(len(self.active) == 1):
            return

        for i in range(len(self.active)-1, 1, -1):
            if(self.active[i].pathcost > self.active[i-1].pathcost):
                self.active[i], self.active[i-1] = self.active[i-1], self.active[i]



    def expand(self, expandNode : Node) -> None:
        """ Creates the current node's children.

        Args:
            expandNode (Node): Node that we want to expand.

        Returns:
            None. Function modifies the activeNodes and the visitedStates lists.
        """
        emptyIndex = expandNode.state.board.index(0)
        emptyRow = emptyIndex // 3
        emptyCol = emptyIndex % 3

        for index in range(len(expandNode.state.board)):

            currRow = index // 3
            currCol = index % 3

            # if (((abs(currRow - emptyRow)) == 1) and (abs(currCol - emptyCol) == 1)):
            if (distance(index, emptyIndex) == 1):
                newState = expandNode.state.board[:]
                newState[index], newState[emptyIndex] = newState[emptyIndex], newState[index]
                verticalMove = currRow - emptyRow
                horizontalMove = currCol - emptyCol

                if(verticalMove < 0):
                    move = "down"
                elif(verticalMove > 0):
                    move = "up"
                elif(horizontalMove < 0):
                    move = "right"
                elif(horizontalMove > 0):
                    move = "left"

                newNode = Node(newState, expandNode.state.goal, 1, expandNode, expandNode.depth + 1, move)
                if(newNode not in self.visited):
                    self.insertActive(newNode)
                    self.totalNodes += 1
        self.visited.append(expandNode)

    def aStarSearch(self) -> list:
        """ Calculates shortest path to goal state

        Returns:
            A list with the shortest path from the initial state to goal state.
        """
        while(len(self.active) > 0):

            nodeToExpand = self.active.pop()

            if(nodeToExpand.state.board == nodeToExpand.state.goal):
                parent = nodeToExpand.parent
                moves = []
                pathcosts = []

                while(parent != None):
                    moves.insert(0, nodeToExpand.move)
                    pathcosts.insert(0, nodeToExpand.pathcost)
                    nodeToExpand = nodeToExpand.parent
                    parent = nodeToExpand.parent

                return [moves, pathcosts, self.totalNodes]
            
            self.expand(nodeToExpand)

        return 0



