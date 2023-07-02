
def find_parent(parent, x):
    
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,  b):
    
    a = find_parent(parent, a)
    b = find_parent(parent, a)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 
    
    


N, M = map(int, input().split())

parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i 
    


for i in range(M):
    num, a, b = map(int, input().split())
    
    if num == 0:
        union_parent(parent, a, b)
    elif num == 1:
        if parent[a] == parent[b]:
            print("YES")
        else:
            print("NO")

