import graphSearch_graph
import graphSearch_node
import graphSearch_csvReader
import random
import math
import graphSearch_obstacle
from shapely.geometry import LineString, Point

def is_node_in_obtacle(x, y, obtsacle):
   """Check the node is inside a obtacle"""
   return ((x - obtsacle.x)**2 + (y-obtsacle.y)**2 <= (obtsacle.diameter/2)**2)  

def is_node_in_graph_obstacles(x, y, graph):
    """Check nodes if it is in any of graph obstacles"""
    for iter in range(len(graph.obstacles)):
        if(is_node_in_obtacle(x,y,graph.obstacles[iter]) == True):
            return True
    return False

def make_A_random_node(graph, x_start, x_end):
    """Generate nodes in graph between x_start and x_end and check if it does not located in graph"""
    check_obstacle = True
    while(check_obstacle != False):
        x = round(random.uniform(x_start[0], x_end[0]), 3)
        y = round(random.uniform(x_start[1], x_end[1]), 3)
        check_obstacle = (is_node_in_graph_obstacles(x, y, graph))
    return [x, y]


def is_nodesCandidate_edge_hit_obstacle(x,y, node, obstacle):
    """Check whether the connecting edges hitting an obtacle"""
    line = LineString([(x,y),(node.position[0], node.position[1])])
    circle = Point(obstacle.x, obstacle.y).buffer(obstacle.diameter/2)
    intersection = line.intersection(circle)
    if intersection.is_empty:
        return False
    else:
        return True

def is_nodeCandidate_endge_hits_obtacles(x,y, node, obstacles):
    """Check whether the connecting edges hitting any obstacles in graph"""
    for obstacle in obstacles.values():
        if is_nodesCandidate_edge_hit_obstacle(x, y, node, obstacle):
            return True
    return False

def calculate_nodeCandidate_distance(x,y, node):
    """Calculate the distance between x, y position and a node"""
    return math.sqrt((x-node.position[0])**2 + (y -node.position[1])**2)

def calculate_two_position_distance(pos1, pos2):
    """Calculate the distance between two position including [x,y]"""
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def find_closest_node_with_weight(x,y,graph):
    """Find the closest node of tree from the random candidate node"""
    node_distances = []
    for node_id in graph.nodes.keys():
       if not is_nodeCandidate_endge_hits_obtacles(x, y, graph.nodes[node_id], graph.obstacles):
         node_distances.append((graph.nodes[node_id].id, calculate_nodeCandidate_distance(x, y, graph.nodes[node_id])))
    sorted_distances = sorted(node_distances, key=lambda x: x[1])
    if(sorted_distances):
        return(sorted_distances[0])
    else:
        return False

def run_algorithm(graph, position_start, position_end, tree_size):
    """Algorithm for Rapidly Exploring Random Tree"""
    tree_node = 2
    graph.add_node(1)
    graph.add_position(1, position_start[0], position_start[1])
    graphSearch_csvReader.print_nodes(1, position_start[0], position_start[1], 0)
    while tree_node < tree_size:
        node_weight = False
        while not node_weight:
            candidate_position = make_A_random_node(graph, position_start, position_end)
            node_weight = find_closest_node_with_weight(candidate_position[0], candidate_position[1], graph)
        graph.add_node(tree_node)
        dist_to_end = calculate_two_position_distance(candidate_position, position_end)
        graph.add_position(tree_node, candidate_position[0], candidate_position[1])
        graphSearch_csvReader.print_nodes(tree_node, candidate_position[0], candidate_position[1], dist_to_end)
        graph.add_edge(tree_node, node_weight[0], node_weight[1])
        if (dist_to_end < 0.1):
            print(candidate_position)
            end_node_id = len(graph.nodes)+1
            graph.add_node(end_node_id)
            graph.add_position(end_node_id, position_end[0], position_end[1])
            graphSearch_csvReader.print_nodes(end_node_id, position_end[0], position_end[1], dist_to_end)
            graph.add_edge(tree_node, end_node_id, dist_to_end)
            print("SUCCESS")
            print(tree_node)
            return True
        tree_node = tree_node + 1
    print("FAILURE")
    return False