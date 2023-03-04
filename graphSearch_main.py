import graphSearch_csvReader
import graphSearch_graph

g = graphSearch_graph.Graph()
graphSearch_csvReader.obstacle_extractor(g)

for iter in range(len(g.obstacles)):
    