// 다익스트라를 쓰는 케이스와 플로이드 워셜을 쓰는 케이스를 구분할 수 있어야 한다
// 자기 자신으로 가는 거리는 0으로 초기화 해야 한다

INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            

if graph[1][X] == INF or graph[X][K] == INF:
    print(-1)
else:
    print(graph[1][K]+graph[K][X])


