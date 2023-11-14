class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def dfs(self, start_vertex, visited):
        visited[start_vertex] = True
        print(start_vertex, end=' ')

        if start_vertex in self.graph:
            for neighbor in self.graph[start_vertex]:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

if __name__ == '__main__':
    g = Graph()
    
    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    num_vertices = max(max(g.graph.keys()) + 1, 1)  # Find the number of vertices
    visited = [False] * num_vertices

    start_vertex = 0  # Start DFS from vertex 0
    print("Depth-First Search (DFS) starting from vertex", start_vertex)
    g.dfs(start_vertex, visited)
