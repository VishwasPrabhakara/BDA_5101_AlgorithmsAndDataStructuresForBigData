from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1

    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

if __name__ == '__main__':
    num_vertices = 6
    g = Graph(num_vertices)

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)

    start_vertex = 0  # Start BFS from vertex 0
    print("Breadth-First Search (BFS) starting from vertex", start_vertex)
    g.bfs(start_vertex)
