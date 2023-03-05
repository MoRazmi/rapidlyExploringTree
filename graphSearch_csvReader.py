import csv
import graphSearch_graph

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
     with open(file_path, 'a', newline='') as csv_file:
          csv_writer = csv.writer(csv_file)
          csv_writer.writerow(array)

def obstacle_extractor(g):
     """Extract obstacles after read csv file"""
     obstacle_data = []
     obstacle_data = read_csv_file('environment/obstacles.csv', obstacle_data)
     for row in range(len(obstacle_data)):
         g.add_obstacle(row, float(obstacle_data[row][0]), float(obstacle_data[row][1]), float(obstacle_data[row][2]))
  
def print_edges(node1, node2, weight):
     edge_toSave = [node1, node2, weight]
     write_csv_file('environment/edges.csv', edge_toSave)

def print_nodes(node_id, x, y, heur):
     node_toSave = [node_id, x, y, heur]
     write_csv_file('environment/nodes.csv', node_toSave)

def result_printer(path):
     write_csv_file('results/path.csv', path)