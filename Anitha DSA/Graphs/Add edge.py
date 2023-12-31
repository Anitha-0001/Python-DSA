class Graphs:
    def __init__(self):
        self.add_list={}
        
    def print_graph(self):
        for vertex in self.add_list:
            print(vertex,":", self.add_list[vertex])      
    
    def add_vertex(self,vertex):
        if vertex not in self.add_list.keys():
            self.add_list[vertex]=[]
            return True
        return False
                        
    def add_edge(self,v1,v2):
        if v1 in self.add_list.keys() and v2 in self.add_list.keys():
            self.add_list[v1].append(v2)
            self.add_list[v2].append(v1)
            return True
        return False
    
my_graph=Graphs()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_edge(1,2)

my_graph.print_graph()