str = input()

x = int(str[1])
y = ord(str[0])-96

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, -2, 2, -2, 2, 1, -1]

ans = 0 

for i in range(0, 8):
    cx = x + dx[i]
    cy = y + dy[i]
    
    if 1<=cx and cx<= 8 and 1<=cy and cy<=8:
        ans += 1

print(ans)
        
