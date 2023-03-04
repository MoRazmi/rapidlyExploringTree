import csv
#import graphSearch_graph

def read_csv_file(file_path, data):
     """Read csv file and ignore the comment line"""
     with open(file_path) as csv_file:
          csv_reader = csv.reader(csv_file)
          for row in csv_reader:
               if not row or row[0].startswith('#'):
                    continue
               data.append(row)
     return data

def write_csv_file(file_path, array):
     with open(file_path, 'w', newline='') as csv_file:
          csv_writer = csv.writer(csv_file)
          csv_writer.writerow(map(lambda x:x, array))

def obstacle_extractor():
     """Extract obstacles after read csv file"""
     obstacle_data = []
     obstacle_data = read_csv_file('environment/obstacles.csv', obstacle_data)
     for row in range(len(obstacle_data)):
          print(obstacle_data[row][0])

def node_extraxor(g):
    """Extract nodes after read csv file"""
    node_data = []
    node_data = read_csv_file('results/nodes.csv', node_data)
    for row in range(len(node_data)):
        g.add_node(int(node_data[row][0]))
        g.add_position(int(node_data[row][0]), float(node_data[row][1]), float(node_data[row][2]))
        g.add_heuristic_cost(int(node_data[row][0]),float(node_data[row][3]))
#        node = graphSearch_AStart.Node(id, position, heuristic_cost)
#        g.add_node(node)

def edge_extractor (g):
    """Extract edges after read csv file"""
    edge_data = []
    edge_data = read_csv_file('results/edges.csv', edge_data)
    for row in range(len(edge_data)):
        g.add_edge(int(edge_data[row][0]), int(edge_data[row][1]), edge_data[row][2])
  
def result_printer(path):
     write_csv_file('results/path.csv', path)