class graph:
    def __init__(self):
        self.graph = {}
    
    def addNode(self, key, val):
        if key not in self.graph:
            self.graph[key] = [val]
        else:
            self.graph[key].append(val)
        
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, vertex):
        visited = set()
        self.DFSUtil(vertex, visited)
                

g = graph()
g.addNode(1, 2)
g.addNode(1, 4)
g.addNode(1, 3)
g.addNode(2, 5)
g.addNode(2, 4)
g.addNode(3, 6)
g.addNode(4, 3)
g.addNode(4, 6)
g.addNode(4, 7)
g.addNode(5, 4)
g.addNode(5, 7)
g.addNode(6, 6)
g.addNode(7, 6)
vert = int(input("Start from vertex: "))
print("Following is Depth First Traversal from Vertex {}:".format(vert))
g.DFS(vert)
print()