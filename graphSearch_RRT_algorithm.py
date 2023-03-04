import graphSearch_graph
import graphSearch_node
import random
import math
import graphSearch_obstacle
from shapely.geometry import LineString, Point

def is_node_in_obtacle(x, y, obtsacle):
   return ((x - obtsacle.x)**2 + (y-obtsacle.y)**2 <= (obtsacle.diameter/2)**2)  

def is_node_in_graph_obstacles(x, y, graph):
    for iter in range(len(graph.obstacles)):
        if(is_node_in_obtacle(x,y,graph.obstacles[iter]) == True):
            return True
    return False

def make_A_random_node(graph, x_start, x_end):
    check_obstacle = True
    while(check_obstacle != False):
        x = round(random.uniform(x_start[0], x_end[0]), 3)
        y = round(random.uniform(x_start[1], x_end[1]), 3)
        check_obstacle = (is_node_in_graph_obstacles(x, y, graph))
    return [x, y]


def is_nodesCandidate_edge_hit_obstacle(x,y, node, obstacle):
    line = LineString([(x,y),(node.position.x, node.position.y)])
    circle = Point(obstacle.x, obstacle.y).buffer(obstacle.diameter/2)
    intersection = line.intersection(circle)
    if intersection.is_empty:
        return False
    else:
        return True

def is_nodeCandidate_endge_hits_obtacles(x,y, node, obstacles):
    for obst_iter in range(obstacles):
            is_nodesCandidate_edge_hit_obstacle(x,y, node, obstacles[obst_iter] )

def calculate_nodeCandidate_distance(x,y, node):
    return math.sqrt((x-node.position.x)**2 + (y - y.node.position.y)**2)

def find_closest_node_with_weight(x,y,graph):
    node_distances = {}
    for iter in range(len(graph.nodes)):
        if not is_nodeCandidate_endge_hits_obtacles(x,y,graph.nodes[iter], graph.obstacles):
            node_distances.append(graph.nodes[iter].id, calculate_nodeCandidate_distance(x,y, graph.nodes[iter]))
    sorted_ditances = sorted(node_distances, key=lambda x: x[1])
    return(sorted_ditances[0])

def run_algorithm(graph, position_start, position_end):
    candidate_position = make_A_random_node(graph, position_start, position_end)
    node_weight = find_closest_node_with_weight(candidate_position[0], candidate_position[1])
    graph.add_node(1)
    graph.add_position(1, candidate_position[0], candidate_position[1])
    graph.add_edge(1, node_weight[0], node_weight[1])