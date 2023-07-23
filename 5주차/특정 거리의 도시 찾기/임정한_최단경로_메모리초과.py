N, M, K, X = map(int, input().split())
info = {}
graph = [[1e9 for _ in range(N)] for _ in range(N)]
for i in range(M):
    src, dst = map(int, input().split())
    info[src-1] = dst-1
    graph[src-1][dst-1] = 1
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = []
for i in range(len(graph[X])):
    if K == graph[X-1][i]:
        answer.append(i)
# print(graph)
if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i]+1)