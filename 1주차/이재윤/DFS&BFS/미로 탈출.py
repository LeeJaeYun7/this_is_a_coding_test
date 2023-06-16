from collections import deque

N, M = map(int, input().split())

board = []
check = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    board.append(list(map(int, input())))


def bfs(x, y):
    
    q = deque()
    check[x][y] = 1
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        
        if x == N-1 and y == M-1:
            break
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx < N and 0<=ny and ny < M and board[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                q.append((nx,ny))

    
bfs(0, 0)


print(check[N-1][M-1])
