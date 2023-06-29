// 우선순위 큐 사용법을 익히자
// distance, dist를 일관성 있게 사용해야 한다
// dijkstra 함수를 호출해야 한다 

import heapq 

INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]


for i in range(1, M+1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    

distance = [INF]*(N+1)

distance[C] = 0 


def dijkstra(start):
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = distance[now]+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    

dijkstra(C)

ans = 0
time = 0 

for i in range(1, N+1):
    if i == C:
        continue
    else:
        if distance[i] != INF:
            ans += 1
            time = max(time, distance[i])
            
print(ans, time) 

