class Graphs:
    def __init__(self):
        self.add_list={}
        
    def print_graph(self):
        for vertex in self.add_list:
            print(vertex, ":", self.add_list[vertex])
            
    def add_vertex(self,vertex):
        if vertex not in self.add_list.keys():
            self.add_list[vertex]=[]
            return True
        return False
    
my_graph = Graphs()
my_graph.add_vertex("A")
my_graph.print_graph()    