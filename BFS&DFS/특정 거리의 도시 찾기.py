from collections import deque 

answer = [] 

N, M, K, X = map(int, input().split())

edges = [[] for _ in range(N+1)]

def bfs(N, start, K, edges):
    
    global answer
    
    visited = [False]*(N+1)

    q = deque()
    q.append([start, 0])
    visited[start] = True
    
    while q:
        num, dist = q.popleft()
     
        if dist == K:
            answer.append(num)
        
        if dist == K+1:
            break
        
        nextCities = edges[num]
        
        for next in nextCities:
            if visited[next] == False:
                q.append([next, dist+1])
                visited[next] = True 
    

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    
bfs(N, X, K, edges)
if len(answer) == 0:
    answer.append(-1)
    
answer.sort() 
for num in answer:
    print(num, end='\n')
