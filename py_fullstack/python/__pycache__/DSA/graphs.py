'''Graph

A graph is a common data structure that consists of a finite set of nodes (or vertices) and a set of edges connecting them.

A pair (x,y) is referred to as an edge, which communicates that the x vertex connects to the y vertex.


Types of graphs:

Undirected Graph:

In an undirected graph, nodes are connected by edges that are all bidirectional. For example if an edge connects node 1 and 2, we can traverse from node 1 to node 2, and from node 2 to 1.

Directed Graph

In a directed graph, nodes are connected by directed edges - they only go in one direction. For example, if an edge connects node 1 and 2, but the arrow head points towards 2, we can only traverse from node 1 to node 2 not in the opposite direction.


Type of Graph Representations:

Adjacency List

To create an Adjacency list, an array of lists is used.
The size of the array is equal to the number of nodes. 
A single index, array[i] represents the list of nodes adjacent to the ith node.
'''