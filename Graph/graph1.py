class Graph:
    def __init__(self,Nodes,is_directed=False):
        self.nodes=Nodes
        self.adj_list={}
        self.is_directed=is_directed
#         print(is_directed)
        
        for node in self.nodes:
            self.adj_list[node]=[]
            
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        
        
        if not self.is_directed:
            self.adj_list[v].append(u)
        
    def degree(self,node):
        deg = len(self.adj_list[node])
        return deg
        
        
    def print_adj_lst(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])

all_edges=[
    ("A","B"),("A","C"),("B","C"),("C","D"),("C","E"),("D","E")
]
nodes=["A","B","C","D","E"]

graph=Graph(nodes)
# graph.print_adj_lst()
for u,v in all_edges:
    graph.add_edge(u,v)
    
graph.add_edge("A","B")
graph.print_adj_lst()
print("Find The Degree Of E :",graph.degree("E"))