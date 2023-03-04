import graphSearch_node
import graphSearch_csvReader

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        """Add a node new node to the graph with three new parameters: ID, Position"""
        self.nodes[id] = graphSearch_node.Node(id)
    
    def add_position(self, node1 , x, y):
        """Add a position x and y coordinates"""
        self.nodes[node1].add_position(x, y)
    
    def add_edge(self, node1, node2, weight = 0):
        """Add edge in the graph connecting first node to second node with weight connecting them"""
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_edge(node2, weight)
        self.nodes[node2].add_edge(node1, weight)

    def close_node(self, node):
        self.nodes[node].close_node()