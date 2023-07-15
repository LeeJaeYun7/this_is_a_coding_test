// 숫자와 문자가 섞여 있을 때는, input().split()으로 입력 받고,
// 숫자를 int형으로 변환해서 처리한다 

N = int(input())
board = [[0]*N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

K = int(input())
info = [] 

def checkMyBody(snake, nx, ny):
    
    for i in range(1, len(snake)):
        if snake[i][0] == nx and snake[i][1] == ny:
            return True 
    
    return False
    
    
for i in range(K):
    x, y = map(int,input().split())
    board[x-1][y-1] = 1 
    
    
L = int(input())

for i in range(L):
    time, dir = input().split()
    info.append((int(time), dir))
    
    
snake = []
snake.append((0,0))
dir = 0 
time = 0 

while True: 
    
    time += 1 
    
            
    x = snake[0][0]
    y = snake[0][1]
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if 0<=nx and nx < N and 0<=ny and ny < N:
        res = checkMyBody(snake, nx, ny)
        
        if res == True:
            break
        
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            snake.insert(0, (nx,ny))
        else:
            snake.insert(0, (nx,ny))
            snake.pop(len(snake)-1)
        
    else:
        break
        
    for i in range(len(info)):
        if info[i][0] == time:
            if info[i][1] == 'L':
                dir -= 1
                if dir == -1:
                    dir = 3 
            elif info[i][1] == 'D':
                dir += 1 
                if dir == 4:
                    dir = 0 



print(time)
    
    
