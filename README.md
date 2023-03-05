Introduction:
This software architecture is designed to implement the RRT algorithm in Python for motion planning of robots or other objects in a complex environment. The RRT algorithm is used to generate feasible paths from a starting configuration to a goal configuration in a dynamic and complex environment.
![Result_screenshot](https://user-images.githubusercontent.com/96496279/222940489-67e2d0a5-fb27-4510-9b92-dcb65b993c3a.png)



Files and Usage:

graphSearch_main.py: This file is the main driver file to run the RRT algorithm. The file requires the starting and ending nodes to be provided and initializes the first node. To run the algorithm, execute this file.

graphSearch_node.py: This file defines the Node class, which contains the x, y, and id attributes. It is used to create a node and add edges between nodes with the desired weight.

graphSearch_obstacle.py: This file defines the Obstacle class, which contains the x, y, and diameter attributes. It is used to define the obstacles in the environment.

graphSearch_csvReader.py: This file defines the CSVReader class, which reads and writes on the path and resets the CSV folder.

graphSearch_graph.py: This file defines the Graph class, which contains the objects to nodes and obstacles. It also has function APIs to add edges and positions, and add nodes and obstacles.

graphSearch_RRT_algorithm.py: This file contains the main algorithm of the RRT. It is based on the following pseudocode:
Algorithm BuildRRT
Input: Initial configuration qinit, number of vertices in RRT K, incremental distance Δq
Output: RRT graph G

G.init(qinit)
for k = 1 to K do
qrand ← RAND_CONF()
qnear ← NEAREST_VERTEX(qrand, G)
qnew ← NEW_CONF(qnear, qrand, Δq)
G.add_vertex(qnew)
G.add_edge(qnear, qnew)
return G

To use this software architecture, follow these steps:

Clone or download the repository to your local machine.
Open the terminal/command prompt and navigate to the downloaded repository.
Execute the graphSearch_main.py file to run the algorithm.
Provide the starting and ending nodes.
The algorithm will generate a feasible path from the starting to the ending node in a dynamic environment.
Conclusion:
This software architecture provides an easy-to-use and efficient implementation of the RRT algorithm in Python. It can be used to generate feasible paths for robots or other objects moving in a complex and dynamic environment. Feel free to modify and use the code according to your needs.
