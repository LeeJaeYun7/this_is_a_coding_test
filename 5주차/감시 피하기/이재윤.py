
N = int(input())
board = []
teachers = [] 
avoidable = False 
exist = False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tmp = list(input().split())
    board.append(tmp)
    
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i,j))
                    
        
def checkStudent(x, y, dir):
    
    global avoidable 
    
    if board[x][y] == 'O':
        return 
    
    if board[x][y] == 'S':
        avoidable = False 
        return 
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if 0<=nx and nx<N and 0<=ny and ny < N:
        checkStudent(nx, ny, dir)
    
    


def dfs(sx, sy, cnt):
    
    if cnt == 3:
        
        global avoidable
        global exist
        
        avoidable = True
        
        for teacher in teachers:
            x = teacher[0]
            y = teacher[1]
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0<=nx and nx < N and 0<=ny and ny <N:
                    checkStudent(nx, ny, k)
                
        
        if avoidable == True:
            exist = True
                
        return 
            
            
        
    
    for i in range(N):
        for j in range(N):
            if ((i==sx and j>sy) or (i>sx)) and board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(i, j, cnt+1)
                board[i][j] = 'X'
        


    
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            board[i][j] = 'O'
            dfs(i, j, 1)
            board[i][j] = 'X'
            

if exist == True:
    print("YES")
else:
    print("NO")
            
            
