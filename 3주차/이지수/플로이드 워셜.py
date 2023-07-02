# 다익스트라와 다른점
# 다익스트라는 한 노드에서 다른 노드까지의 최소 경로를 계산하는 알고리즘이라면
# 플로이드 워셜 알고리즘은 모든 노드에서 다른 모든 노드까지의 최소 경로를 계산하는 알고리즘이다.
# 다익스트라는 그리디를, 플로이드 워셜은 다이나믹 프로그래밍 알고리즘을 베이스로 하고 있으며
# 시간복잡도는 다익스트라(개선된 다익스트라) - O(V**2) (O(ElogV)) / 플로이드워셜 - O(N**3)

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range( 1, n+1):
    for b in range(1, n+1):
        # 도달 할 수 없는 경우 무한 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()