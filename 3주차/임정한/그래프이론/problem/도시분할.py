def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: # 앞쪽 index의 parent로
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())


class CityDivisor:
    def __init__(self):
        self.parent = [i for i in range(n)]
        self.edges = []
        self.result = 0

        for _ in range(m):
            a, b, cost = map(int, input().split())
            self.edges.append((cost, a-1, b-1))
        self.edges.sort()

        record = None

        for edge in self.edges:
            cost, a, b= edge

            if find_parent(self.parent, a)!= find_parent(self.parent, b):
                union_parent(self.parent, a, b)
                self.result += cost
                record = cost

        print(self.result - record)
CityDivisor()