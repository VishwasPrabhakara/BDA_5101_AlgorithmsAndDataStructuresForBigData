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

    def dfs(self, vertex, visited, connected_component):
        visited[vertex] = True
        connected_component.append(vertex)

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if not visited.get(neighbor):
                    self.dfs(neighbor, visited, connected_component)

    def connected_components(self):
        visited = {}
        components = []

        for vertex in self.graph:
            if not visited.get(vertex):
                connected_component = []
                self.dfs(vertex, visited, connected_component)
                components.append(connected_component)

        return components

if __name__ == '__main__':
    g = Graph()

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(6, 7)

    connected_components = g.connected_components()
    for i, component in enumerate(connected_components):
        print(f"Connected Component {i + 1}: {component}")
