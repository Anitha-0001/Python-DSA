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
    
    def remove_edge(self,v1,v2):
        if v1 in self.add_list.keys() and v2 in self.add_list.keys():
            try:
                self.add_list[v1].remove(v2)
                self.add_list[v2].remove(v1) 
            except ValueError:
                pass
            return True
        return False    
    
    def remove_vertex(self,vertex):
        if vertex in self.add_list.keys():
            for other_vertex in self.add_list[vertex]:
                self.add_list[other_vertex].remove(vertex)
            del self.add_list[vertex]
            return True
        return False

    
my_graph=Graphs()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("D","B")
my_graph.add_edge("D","C")

my_graph.remove_vertex("D")
my_graph.print_graph()
