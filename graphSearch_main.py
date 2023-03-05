import graphSearch_csvReader
import graphSearch_graph
import graphSearch_RRT_algorithm

g = graphSearch_graph.Graph()
graphSearch_csvReader.obstacle_extractor(g)
x_start = [-0.5, -0.5]
x_end = [0.5, 0.5]
g.add_node(1)
g.add_position(1, -0.5, -0.5)

graphSearch_RRT_algorithm.run_algorithm(g, x_start, x_end, 100)