from queue import Queue


class Vertex:
    def __init__(self, value, adjacent_vertices=None):
        self.value = value
        self.vertices = {}
        if adjacent_vertices is None:
            self.adjacent_vertices = []

    def add_adjacent_vertices(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertices(self)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.value] = vertex

    def dfs_traverse(self, start_vertex, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = {}
        visited_vertices[start_vertex.value] = True
        print(start_vertex.value)

        for adjacent_vertex in start_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                self.dfs_traverse(start_vertex=adjacent_vertex, visited_vertices=visited_vertices)

    def bfs_traverse(self, start_vertex, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = {}
        queue = Queue()
        visited_vertices[start_vertex.value] = True
        queue.enqueue(element=start_vertex)

        while queue.read():
            current_vertex = queue.dequeue()
            print(current_vertex.value)
            for adjacent_vertex in current_vertex.adjacent_vertices:
                if adjacent_vertex.value not in visited_vertices:
                    visited_vertices[adjacent_vertex.value] = True
                    queue.enqueue(element=adjacent_vertex)


alice = Vertex(value='Alice')
bob = Vertex(value='Bob')
george = Vertex(value='George')
kelly = Vertex(value='Kelly')

graph = Graph()
graph.add_vertex(alice)
graph.add_vertex(bob)
graph.add_vertex(george)
graph.add_vertex(kelly)

alice.add_adjacent_vertices(vertex=george)
george.add_adjacent_vertices(vertex=bob)
kelly.add_adjacent_vertices(vertex=alice)

graph.dfs_traverse(start_vertex=alice)
print('=======')
graph.bfs_traverse(start_vertex=alice)
