from typing import List, Dict

MAXSIZE = 1000000
from collections import defaultdict


class MatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacent_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def __len__(self):
        return self.num_vertices

    def add(self, src, dest, weight):
        self.adjacent_matrix[src][dest] = weight


class DictGraph:
    def __init__(self, num_vertices = None):
        self.adjacent_dict = defaultdict(list)

    def __call__(self, *args, **kwargs):
        return self.adjacent_dict

    def __len__(self):
        return len(self.adjacent_dict)

    def add(self, src, dest, weight):
        self.adjacent_dict[src].append((dest, weight))

    def add_many(self, vertex: List):
        for vertice in vertex:
            src, dest, weight = vertice
            self.add(src, dest, weight)

    def key(self):
        return self.adjacent_dict.keys()


class ShortestAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find(self, src, target):
        raise NotImplementedError


class Dijkstra(ShortestAlgorithm):
    def __init__(self, graph: DictGraph):
        super().__init__(graph)
        self.number_edge = len(graph)
        self.distance: Dict = {k: MAXSIZE for k in graph.key()}
        self.visited: Dict = {k: False for k in graph.key()}

    def find(self, src, target):
        self.distance[src] = 0
        self.update_distance()
        return self.distance[target]

    def update_distance(self):
        for _ in range(self.number_edge):
            edge = self._get_nearest_edge()
            self.visited[edge] = True
            for neighbor in self.graph()[edge]:
                dest, weight = neighbor
                self.distance[dest] = min(self.distance[dest], self.distance[edge] + weight)

    def _get_nearest_edge(self):
        min_distance, min_vertex = min((self.distance[v], v) for v in self.graph.key() if not self.visited[v])
        return min_vertex


if __name__ == "__main__":
    given_map = [(1, 4, 1), (2, 4, 1), (3, 2, 1), (4, 5, 1), (4, 1, 1), (4, 2, 1), (2, 3, 1), (5, 4, 1), (5, 6, 12), (6, 5, 1)]
    graph = DictGraph()
    graph.add_many(given_map)
    route = Dijkstra(graph)
    print(route.find(1, 6))

    #FIXME: Only dst -> src cannot record key