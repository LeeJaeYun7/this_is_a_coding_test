// pypy3로 채점함
// 최단거리이므로, bfs로 접근함

from collections import deque

N, M, K, X = map(int, input().split()) 

arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)


def bfs(start):
    
    q = deque()
    q.append(start)
    visited[start] = 1 
    
    
    while q:
        num = q.popleft()
        
        for next in arr[num]:
            if visited[next] == 0:
                visited[next] = visited[num] + 1 
                q.append(next) 




bfs(X)

isExist = False

for i in range(1, N+1):
    if visited[i]-1 == K:
        isExist = True 
        print(i)

if isExist == False:
    print(-1)


