#!/usr/bin/python3

from node import Node
from board import Board


""" Algorithm Class

    Attributes:
        active (list[Node]): List with the current states of the puzzle to be expanded
        visited (list[Node]) : List with the Nodes that were visited already
    """
class Algorithm:
    def __init__(self, initialNode):
        self.active = []
        self.insertActive(initialNode)
        self.visited = []

    def insertActive(self, stateNode : Node) -> None:
        """ Properly inserts a node in the list of active nodes.

                Args:
                    stateNode (Node): Node that we want to insert into active

                Returns:
                    None. Function modifies the activeNodes and the visitedStates lists.
                """
        self.active.append(stateNode) #Figure out the rest later
        if(len(active) == 1):
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
        emptyIndex = expandNode.board.state.index(0)
        emptyRow = emptyIndex // 3
        emptyCol = emptyIndex % 3

        for index in range(len(expandNode.state)):

            currRow = index // 3
            currCol = index % 3

            if (((abs(currRow - emptyRow)) == 1) or (abs(currCol - emptyCol) == 1)):
                newState = expandNode.board.state
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

                newNode = Node(newState, expandNode.goal, 1, expandNode, expandNode.depth + 1, move)
                if(newNode not in self.visited):
                    self.insertActive(newNode)
        self.visited.append(expandNode)

    def aStarSearch(self) -> list:
        """ Calculates shortest path to goal state

        Returns:
            A list with the shortest path from the initial state to goal state.
        """
        while(len(self.active) > 0):

            nodeToExpand = self.active.pop()

            if(nodeToExpand.state.board == nodeToExpand.state.goal):
                return nodeToExpand

            self.expand(nodeToExpand)

        return 0



