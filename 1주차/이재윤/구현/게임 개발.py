// n, m을 입력 받는다
n, m = map(int, input().split())

// x, y, dir을 입력 받는다
x, y, dir = map(int, input().split())

// visited를 0으로 초기화한다 
visited = [[0]*m for _ in range(n)]

// gameMap 리스트를 선언한다 
gameMap = []

// dx, dy 리스트를 초기화한다 
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

ans = 0 

for i in range(n):
    gameMap.append(list(map(int, input().split())))


gameEnd = False


while True:
    
    // gameEnd가 True이면 break한다     
    if gameEnd == True:
        break
    
    // visited[x][y]에 1을 넣는다 
    visited[x][y] = 1
    // cnt를 0으로 초기화한다 
    cnt = 0 
    
    while True:
        
        // cnt가 4이면 뒤로 가는 검사를 한다  
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
                
            // 뒤가 만약에 바다이면, 게임을 끝낸다
            if gameMap[nx][ny] == 1:
                gameEnd = True
                break
            // 뒤가 만약에 육지이면, 뒤로 이동한다 
            else:
                x = nx
                y = ny
                break
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        
        
        // nx, ny가 gameMap안에 있고, 아직 방문하지 않은 점이라면, 이동한다 
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
        
    
// visited점을 세어서 ans에 더해준다.     
for i in range(0, n):
    for j in range(0, m):
        if visited[i][j] == 1:
            ans += 1
            
            
print(ans) 
    







