#!/usr/bin/python3

""" Object file for the Algorithm class.
    This contains the entire algorithm
    and all execution is done here.
    It is invoked from puzzle8.py.

Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

from board import Board, Node
distance = Board.distance
getRow = Board.getRow
getCol = Board.getCol

class Algorithm:
    """ Algorithm Class

    Attributes:
        active (list[Node]): List with the current states of the puzzle to be expanded
        visited (list[Node]) : List with the Nodes that were visited already
        visitedArrays (list[list[int]]): List with the arrays of the visited states
        totalNodes(Int) : Total amount of nodes generated by the algorithm
    """
    def __init__(self, initialNode):
        self.active = []
        self.insertActive(initialNode)

        self.visited = []
        self.visitedArrays = []
        self.totalNodes = 1


    def insertActive(self, stateNode : Node) -> None:
        """ Properly inserts a node in the list of active nodes.

            Args:
                stateNode (Node): Node that we want to insert into active

            Returns:
                None.
                Function modifies the activeNodes and the visitedStates lists.
        """
        self.active.append(stateNode)
        if(len(self.active) == 1):
            return
        # Move stateNode to the left so that list is organized from biggest to smallest
        for i in reversed(range(1, len(self.active))):
            if(self.active[i].pathcost > self.active[i-1].pathcost):
                self.active[i], self.active[i-1] = self.active[i-1], self.active[i]


    def expand(self, expandNode : Node) -> None:
        """ Creates the current node's children.

        Args:
            expandNode (Node): Node that we want to expand.

        Returns:
            None. 
            Function modifies the activeNodes and the visitedStates lists.
        """
        emptyIndex = expandNode.state.board.index(0)
        emptyRow = getRow(emptyIndex)
        emptyCol = getCol(emptyIndex)

        # Going over all values of the current state that we need to expand
        for index in range(len(expandNode.state.board)):

            currRow = getRow(index)
            currCol = getCol(index)

            # If the distance between the current tile and the empty tile is 1,
            # that means we can obtain new states from there
            if (distance(index, emptyIndex) == 1):
                newState = expandNode.state.board[:]
                newState[index], newState[emptyIndex] = newState[emptyIndex], newState[index]
                verticalMove = currRow - emptyRow
                horizontalMove = currCol - emptyCol

                if(verticalMove < 0):
                    move = "U"
                elif(verticalMove > 0):
                    move = "D"
                elif(horizontalMove < 0):
                    move = "L"
                elif(horizontalMove > 0):
                    move = "R"

                newNode = Node(newState, expandNode.state.goal, expandNode.heuristic, expandNode, expandNode.depth + 1, move)

                # If the new node created hasn't been visited yet,
                # then add it to the list of nodes to expand
                if(newNode.state.board not in self.visitedArrays):
                    self.insertActive(newNode)
                    self.totalNodes += 1

        self.visited.append(expandNode)
        self.visitedArrays.append(expandNode.state.board)


    def aStarSearch(self) -> list:
        """ Calculates shortest path to goal state

        Returns:
            A list with the shortest path from the initial state to goal state.
        """
        # While there are active states in the tree
        while(len(self.active) > 0):

            # This will give us the active node with the smallest f(n)
            nodeToExpand = self.active.pop()
            shallowestD = nodeToExpand.depth

            # If the current node is a goal node
            if(nodeToExpand.state.board == nodeToExpand.state.goal):
                parent = nodeToExpand.parent
                moves = []
                pathcosts = []

                # This loop goes over the solution path to gather the data
                # that the algorithm should return
                while(True):
                    moves.insert(0, nodeToExpand.move)
                    pathcosts.insert(0, nodeToExpand.pathcost)
                    nodeToExpand = nodeToExpand.parent
                    parent = nodeToExpand.parent
                    if parent == None:
                        pathcosts.insert(0, nodeToExpand.pathcost)
                        nodeToExpand = nodeToExpand.parent
                        break

                return [shallowestD, self.totalNodes, moves, pathcosts]
            
            self.expand(nodeToExpand)

        return 0
