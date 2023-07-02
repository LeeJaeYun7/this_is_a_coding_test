// edges에 cost, a, b 순으로 값을 넣어줘야 한다
// 그 다음에 edges를 정렬해줘야 한다
// maxCost는 find_parent가 다를 때만, 업데이트 해야 한다 

def find_parent(parent, x):
    
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    


def union_parent(parent, a, b):
    
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 
    



N, M = map(int, input().split())
parent = [0]*(N+1)

for i in range(1, N+1):
    parent[i] = i 


edges = []
result = 0
maxCost = 0

for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    

edges.sort()


for edge in edges:
    
    cost, a, b = edge 
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        maxCost = max(maxCost, cost)
    

print(result-maxCost)
    
