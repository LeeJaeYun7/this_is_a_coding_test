N = int(input())

x, y = 1, 1

plans = input().split()

for c in plans:
    if c == 'R':
        nx = x
        ny = y + 1
    elif c == 'U':
        nx = x - 1
        ny = y
    elif c == 'L':
        nx = x 
        ny = y - 1
    elif c == 'D':
        nx = x + 1
        ny = y
        
    if 1<=nx and nx <= N and 1<=ny and ny <= N:
        x = nx
        y = ny
    


print (x, y)
