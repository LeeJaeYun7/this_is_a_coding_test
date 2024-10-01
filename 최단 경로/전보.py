import heapq

INF = 1e9

N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z])

distance = [INF]*(N+1)

def dijkstra(start):

    q = []
    heapq.heappush(q, (0, start))

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)
cities = 0
maxDistance = -1e9

for i in range(1, N+1):
    if i == C:
        continue
    cities += 1
    maxDistance = max(maxDistance, distance[i])

print(cities)
print(maxDistance)
