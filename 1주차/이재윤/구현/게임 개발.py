n, m = map(int, input().split())

x, y, dir = map(int, input().split())

visited = [[0]*m for _ in range(n)]

gameMap = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

ans = 0 

for i in range(n):
    gameMap.append(list(map(int, input().split())))


gameEnd = False


while True:
    
    
    if gameEnd == True:
        break
    
    
    visited[x][y] = 1
    cnt = 0 
    
    while True:
        
        
        if cnt == 4:
            
            if dir == 0:
                nx = x+1
                ny = y
            elif dir == 1:
                nx = x
                ny = y-1
            elif dir == 2:
                nx = x-1
                ny = y
            elif dir == 3:
                nx = x
                ny = y+1
                
            
            if gameMap[nx][ny] == 1:
                gameEnd = True
                break
            else:
                x = nx
                y = ny
                break
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        
        
        
        if 0<=nx and nx < n and 0<=ny and ny < m and visited[nx][ny] == 0 and gameMap[nx][ny] == 0:
            x = nx 
            y = ny
            
            if dir == 0:
                dir = 3
            else:
                dir -= 1
            break
        
        else:
            if dir == 0:
                dir = 3
            else: 
                dir -= 1
            
            cnt += 1
        
    
    
for i in range(0, n):
    for j in range(0, m):
        if visited[i][j] == 1:
            ans += 1
            
            
print(ans) 
    







