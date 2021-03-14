import math

class Graph:
    def __init__(self, n, c, nodes_list, connections):
        self.nodes = nself.connections = c 
        self.nodes_list = nodes_list
        self.connections_dict = connections
    def bellman_ford(self, src):
        self.nodes_dict = {k: math.inf for k in self.nodes_list}
        lst = list(self.connections_dict.keys())
        for key in lst:
           temp_lst = key.split(' -')
           temp_lst.reverse()
           self.connections_dict[' -'.join(temp_lst)] = self.connections_dict[key]
           self.nodes_dict[src] = 0
        for i in range(self.nodes -1):
            for connection in self.connections_dict:
                lst = connection.split(' -')
                if (self.nodes_dict[lst[0]] != math.inf) and ((self.nodes_dict[lst[0]] + self.connections_dict[connection]) < self.nodes_dict[lst[-1]]):
                    self.nodes_dict[lst[-1]] = self.nodes_dict[lst[0]] + self.connections_dict[connection]                   
        return self.nodes_dict
   
obj = Graph(7, 10, ['A', 'B', 'C', 'D', 'E', 'F', 'G'], {'A -C': 2, 'A -E': 1, 'E -F': 4, 'F -G': 2, 'G -D': 1, 'D -C': 8, 'D -B': 13, 'B -C': 2, 'B -F': 2, 'B -E': 1})
print(‘Distance of other nodes from source node A:’, obj.bellman_ford(‘A’))
print(‘Distance of other nodes from source node B:’, obj.bellman_ford(‘B’))
print(‘Distance of other nodes from source node C:’, obj.bellman_ford(‘C’))
print(‘Distance of other nodes from source node D:’, obj.bellman_ford(‘D’))
print(‘Distance of other nodesfrom source node E:’, obj.bellman_ford(‘E’))
print(‘Distance of other nodes from source node F:’, obj.bellman_ford(‘F’))
print(‘Distance of other nodes from source node G:’, obj.bellman_ford(‘G’))
