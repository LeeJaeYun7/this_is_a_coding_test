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

class TeamResolver():
    def __init__(self):
        self.parent = [i for i in range(n)]

    def operate(self, command, a, b):
        if command == 0:
            union_parent(self.parent, a, b)
        if command == 1:
            if find_parent(self.parent, a) == find_parent(self.parent, b):
                print("YES")
            else:
                print("NO")

resolve = TeamResolver()
for i in range(m):
    oper, a, b = map(int, input().split())
    resolve.operate(oper, a-1, b-1)
