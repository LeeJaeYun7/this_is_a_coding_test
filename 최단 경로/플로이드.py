INF = int(1e9)

n = int(input())
m = int(input())

cost = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    if cost[a][b] > c:
        cost[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            cost[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF:
            cost[i][j] = 0 
        print(cost[i][j], end=' ')
    print('', end='\n')

