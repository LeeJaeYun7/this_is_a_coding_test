// deque을 활용하기 위해 import를 한다
from collections import deque

// N, M을 입력 받아서 저장한다 
N, M = map(int, input().split())

// board 리스트를 선언한다
board = []

// check 2차원 배열을 0으로 초기화한다
check = [[0]*M for _ in range(N)]

// dx, dy를 선언한다 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

// 2차원 board 리스트를 초기화한다 
for i in range(N):
    board.append(list(map(int, input())))

// bfs를 선언한다 
def bfs(x, y):
    
    // q라는 이름의 덱을 선언한다 
    q = deque()
    // check[x][y] = 1로 초기화한다
    check[x][y] = 1
    // q에 (x,y)를 넣는다 
    q.append((x,y))
    
    // q가 값이 있을 때
    while q:
        // x,y를 q에서 pop한다
        x, y = q.popleft()
        
        // x == N-1 이고 y == M-1이면 끝에 도착했으므로, break 한다 
        if x == N-1 and y == M-1:
            break
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            // board[nx][ny] = 1이고, check[nx][ny] == 0일 때, 
            // check[nx][ny]에 check[x][y]+1을 넣어준다 
            if 0<=nx and nx < N and 0<=ny and ny < M and board[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                q.append((nx,ny))

    
bfs(0, 0)


print(check[N-1][M-1])
