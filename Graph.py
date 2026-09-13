
# ----------------------------------------------GRAPH----------------------------------------------------->>>>>>>>>>>>>>>>>>>
# GRAPH

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)

    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            del self.adjacency_list[vertex]
            return True

        return False

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def displaygraph(self):
        for k,v in self.adjacency_list.items():
            print(k,":",v)
graph = Graph()
#pass the number of vertex
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
# graph.displaygraph()

graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('A','D')
graph.add_edge('B','A')
graph.add_edge('B','E')
graph.add_edge('C','A')
graph.add_edge('C','D')
graph.add_edge('D','A')
graph.add_edge('D','C')
graph.add_edge('D','E')
graph.add_edge('E','B')
graph.add_edge('E','D')

graph.displaygraph()
print()
graph.remove_vertex('C')
print()
graph.displaygraph()
print()
graph.remove_edge('D','A')
print()
graph.displaygraph()

