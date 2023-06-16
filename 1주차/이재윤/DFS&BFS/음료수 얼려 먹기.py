
N, M = map(int, input().split())
graph = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y, graph):
    
    graph[x][y] = 1
    
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx and nx < N and 0<=ny and ny < M and graph[nx][ny] == 0:
            dfs(nx, ny, graph)
            


for i in range(N):
    graph.append(list(map(int, input())))
    

iceCream = 0 


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            iceCream += 1
            dfs(i, j, graph)
        
        
print(iceCream)
    
    
        






