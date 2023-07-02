from typing import Dict

n, m = map(int, input().split())
INF = int(1e9)


class ShortestPath:
    def __init__(self):
        self.k = None
        self.x = None
        self.visited = [False for i in range(n)]
        self.adjacent_matrix = [
            [INF if i != j else 0 for i in range(n)] for j in range(n)
        ]

    def get_input(self):
        for _ in range(m):
            a, b = map(int, input().split())
            self.adjacent_matrix[a - 1][b - 1], self.adjacent_matrix[b - 1][a - 1] = (
                1,
                1,
            )

    def floyd_warshall(self):
        for x in range(n):
            for i in range(n):
                for j in range(n):
                    self.adjacent_matrix[i][j] = min(
                        self.adjacent_matrix[i][j],
                        self.adjacent_matrix[i][x] + self.adjacent_matrix[x][j],
                    )

    def distance(self, src, dst):
        return self.adjacent_matrix[src][dst]

sp = ShortestPath()
sp.get_input()
x, k = map(int, input().split())
sp.floyd_warshall()
if sp.distance(0, x-1) >=INF or sp.distance(x-1, k-1) >=INF:
    print(-1)
else:
    print(sp.distance(0, k-1)+sp.distance(k-1, x-1))
# print(sp.adjacent_matrix)
