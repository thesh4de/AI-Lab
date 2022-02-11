class graph:
    def __init__(self):
        self.graph = {}
    
    def addNode(self, key, val):
        if key not in self.graph:
            self.graph[key] = [val]
        else:
            self.graph[key].append(val)
        
    def BFS(self, x):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(x)
        visited[x] = True
        while queue:
            x = queue.pop(0)
            print(x, end=" ")
            for i in self.graph[x]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                

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
print("Following is Breadth First Traversal from Vertex {}:".format(vert))
g.BFS(vert)
print()