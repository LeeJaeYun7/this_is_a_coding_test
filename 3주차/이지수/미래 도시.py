import sys
sys.stdin = open("input2.txt")
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 - 자기자신 비용은 0으로
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# graph 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 중요
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
    
    
# 코드 흐름 & 점화식 구현 코드를 외울 것
# 노드의 범위가 매우 한정적(100이하) 이라면 플로이드 워셜 알고리즘을 고려한다.