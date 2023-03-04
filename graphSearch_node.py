from enum import Enum

class node_position:
     """The 2D position represent the position of a node in a 2-dimnesional space."""
     def __init__(self,x, y):
      self.x = x
      self.y = y

INFINITY = 10000

class searchCondition(Enum):
     """Enum defintion for Open and close nodes"""
     CLOSE = True
     OPEN = False

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.position = {}
        
    def add_position(self, x, y):
        """Add x y position of the node"""
        self.position[0] = x
        self.position[1] = y

    def add_edge(self, neighbor, weight =0):
        """Add edge to the node"""
        self.edges[neighbor] = weight


    def close_node(self):
        self.searchConditionClosed = True
