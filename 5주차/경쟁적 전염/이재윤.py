// 2중 for문 안에 j로 쓰는 것을 주의 해야 한다
// list에 값을 담고, deque에 넣어주면 큐로 변할 수 있다
// list에 값이 3개씩 담길 때, 그냥 sort를 해주면, 맨 앞에꺼 기준으로 sort가 된다
// S가 0일 때를 고려 해야 한다
// -> 문제의 조건에 잘 유의해야 한다
// 급하게 풀지 않아야 한다 
// 큐를 2개 선언하는 것보다, 하나로 선언하고 for문으로 도는 것이 좋다

from collections import deque 

N, K = map(int, input().split())

board = [] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []

for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j))


virus.sort()
q = deque(virus)    
time = 0 

while q:

    if time == S:
        break 
    
    
    for i in range(len(q)):
        num, x, y = q.popleft()
        
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            
            if 0<=nx and nx<N and 0<=ny and ny < N and board[nx][ny] == 0:
                board[nx][ny] = num 
                q.append((num, nx, ny))
    
    
    time += 1 
    
   
    

print(board[X-1][Y-1])
    
    
    







