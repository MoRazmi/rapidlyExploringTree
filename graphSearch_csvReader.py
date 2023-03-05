import csv
import graphSearch_graph

"""
Path location for edges, nodes, and obstacles
"""
edges_path = 'environment/edges.csv'
obstacle_path = 'environment/obstacles.csv'
node_path = 'environment/nodes.csv'



def reset_cvs_file(file_path):
     """Erase files to prepare for the results"""
     try:
          with open(file_path, 'w', newline='') as csv_file:
               pass
     except IOError:
          print(f"Error: Could not reset CSV file at {file_path}")

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
     """Write onto csv file new array"""
     with open(file_path, 'a', newline='') as csv_file:
          csv_writer = csv.writer(csv_file)
          csv_writer.writerow(array)

def obstacle_extractor(g):
     """Extract obstacles after read csv file"""
     obstacle_data = []
     obstacle_data = read_csv_file(obstacle_path, obstacle_data)
     for row in range(len(obstacle_data)):
         g.add_obstacle(row, float(obstacle_data[row][0]), float(obstacle_data[row][1]), float(obstacle_data[row][2]))
  
def print_edges(node1, node2, weight):
     """Print edges to the csv file"""
     edge_toSave = [node1, node2, weight]
     write_csv_file(edges_path, edge_toSave)

def print_nodes(node_id, x, y, heur):
     """print nodes to csv file"""
     node_toSave = [node_id, x, y, heur]
     write_csv_file(node_path, node_toSave)
