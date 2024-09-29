N = int(input())

T = []
P = []
maxTotal = 0

def dfs(day, total):

    global N
    global maxTotal

    maxTotal = max(maxTotal, total)

    for i in range(day, N):
        if (i+T[i]) <= N:
            dfs(i+T[i], total+P[i])


for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    if (i+T[i]) <= N:
        dfs(i+T[i], P[i])

print(maxTotal)
