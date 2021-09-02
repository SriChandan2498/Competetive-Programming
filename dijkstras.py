# Write a program that finds the shortest path from a source 
# vertex (0) to all other vertices. Following is a sample 
# input and output files.

# Sample Input:
# 8
# 15
# 4 5 0.35
# 5 4 0.35
# 4 7 0.37
# 5 7 0.28
# 7 5 0.28
# 5 1 0.32
# 0 4 0.38
# 0 2 0.26
# 7 3 0.39
# 1 3 0.29
# 2 7 0.34
# 6 2 0.40
# 3 6 0.52
# 6 0 0.58
# 6 4 0.93

# Sample Output:
#  0 to 0 (0.00)  
#  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
#  0 to 2 (0.26)  0->2  0.26
#  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
#  0 to 4 (0.38)  0->4  0.38
#  0 to 5 (0.73)  0->4  0.38   4->5  0.35
#  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
#  0 to 7 (0.60)  0->2  0.26   2->7  0.34

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

'''
This class defines an Edge
'''
class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for edge in self.edges:
            value = edge.value
            nodefrom = edge.node_from.value
            nodeto = edge.node_to.value
            edge_list.append((value,nodefrom,nodeto))
        return edge_list

    def get_adjacency_list(self):
        max_index = len(self.nodes)
        adjacency_list = [None] * (max_index + 1)
        for edge in self.edges:
            value = edge.value
            nodefrom = edge.node_from.value
            nodeto = edge.node_to.value
            if adjacency_list[nodefrom]:
                adjacency_list[nodefrom].append((nodeto,value))
            else:
                adjacency_list[nodefrom] = [(nodeto,value)]
        return adjacency_list
    
    
    def get_adjacency_matrix(self):
        max_index = len(self.nodes)
        adjacency_matrix = [[0 for i in range(max_index)] for j in range(max_index)]
        for edge in self.edges:
            value = edge.value
            nodefrom = edge.node_from.value
            nodeto = edge.node_to.value
            adjacency_matrix[nodefrom][nodeto] = value
        return adjacency_matrix

class ShortestPaths:
    # Your code goes here...
    def __init__(self,data):
        self.data = data
        self.graph = Graph()

    def shortestpath(self,parent, j,spl):        
        if parent[j] == -1 :
            spl.append(j)
            return
        self.shortestpath(parent , parent[j],spl)
        spl.append(j)
        return spl

    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
    
    def dijkstra(self):
        s = self.data
        l = s.splitlines()
        vertices = int(l[0])
        n = int(l[1])
        l = l[2:]
        for i in range(n):
            v = l[i].split()
            from_node,to_node,edge = v
            self.graph.insert_edge(float(edge), int(from_node), int(to_node))
        
        adj_list = self.graph.get_adjacency_matrix()

        dist = [float("Inf")] * vertices
        parent = [-1] * vertices
        dist[0] = 0
        queue = []
        for i in range(vertices):
            queue.append(i)
        while queue:
            u = self.minDistance(dist,queue)  
            queue.remove(u)
            for i in range(vertices):
                if adj_list[u][i] and i in queue:
                    if dist[u] + adj_list[u][i] < dist[i]:
                        dist[i] = dist[u] + adj_list[u][i]
                        parent[i] = u
        for i in range(1, len(dist)):
            print(f"0 to {i} ",end="(")
            print("{:.2f}".format(dist[i]),end=")  ")
            sp = self.shortestpath(parent,i,spl=[])
            for j in range(1,len(sp)):
                print(f"{sp[j-1]}->{sp[j]}  {adj_list[sp[j-1]][sp[j]]} ",end="  ")
            print()

s = '''8
15
4 5 0.35
5 4 0.35
4 7 0.37
5 7 0.28
7 5 0.28
5 1 0.32
0 4 0.38
0 2 0.26
7 3 0.39
1 3 0.29
2 7 0.34
6 2 0.40
3 6 0.52
6 0 0.58
6 4 0.93'''

shortestpath = ShortestPaths(s)

shortestpath.dijkstra()
