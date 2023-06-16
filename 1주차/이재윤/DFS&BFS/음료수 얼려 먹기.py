
// 초기값 N,M을 입력 받는다
N, M = map(int, input().split())

// graph 리스트를 선언한다 
graph = []

// dx, dy를 선언한다 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

// dfs 함수를 선언한다
def dfs(x, y, graph):
    
    // 해당 x,y 값에 대해, graph[x][y]를 1로 바꾼다
    // 즉, 방문 처리를 한다 
    graph[x][y] = 1
    
    // 4가지 방향을 표현하기 위해 for i in range(4)를 선언한다 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        // nx, ny가 맵 안에 있고, graph[nx][ny]가 방문하지 않은 점일 때, 
        // 방문한다 
        if 0<=nx and nx < N and 0<=ny and ny < M and graph[nx][ny] == 0:
            dfs(nx, ny, graph)
            

// graph 리스트에 입력값을 넣는다
for i in range(N):
    graph.append(list(map(int, input())))
    

iceCream = 0 

// N, M으로 2차원 graph 리스트를 탐색한다
// 이 때, graph[i][j] == 0일때마다, 탐색을 시작하고,
// 아이스크림 개수를 하나 추가한다. 
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            iceCream += 1
            dfs(i, j, graph)
        
        
print(iceCream)
    
    
        






