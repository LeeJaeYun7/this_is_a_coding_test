# BFS ???

import heapq

INF = int(1e9)

n, m, c = map(int, input().split())


class ShortestPathEnvelope():
    def __init__(self):
        self.graph = [[INF if i != j else 0 for j in range(n)] for i in range(n)]
        self.visited = [False for i in range(n)]

