#!/usr/bin/python3

from 8puzzle import *

class Algorithm:
    def __init__(self):
        self.active = []
        self.visited = []

    def insertActive(self, stateNode):
        self.active.append(stateNode) #Figure out the rest later

        for i in range(len(self.active)-1, 1, -1):
            if(self.active[i].pathcost > self.active[i-1].pathcost):
                self.active[i], self.active[i-1] = self.active[i-1], self.active[i]



    def expand(self, expandNode : Node) -> None:
        """ Creates the current node's children.

        Args:
            expandNode (Node): Node that we want to expand.
            activeNodes (list[int]): List of nodes that are yet to be expanded.
            visitedNodes (list[list[int]]): List of already visited nodes.

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
