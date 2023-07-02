# import sys
# input = sys.stdin.readline
# INF = int(1e9) # 무한값. 10억
# 
# n, m = map(int, input().split())

# start = int(input()) #시작노드
# graph = [[] for i in range(n+1)]
# 
# visited = [[False] * (n + 1)] # 방문체크
# distance = [INF] * (n + 1) # 최단거리테이블
# 
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c
#     graph[a].append((b, c))
# 
# # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]: # 방문하지 않은 노드 중 더 짧은 경로가 있는 경우
#             min_value = distance[i]
#             index = i
#     return index
# 
# def dijkstra(start):
#     # 시작 노드에 대해 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
# 
#         for j in graph[now]:
#             cost = distance[now] + j[1]
# 
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# 
# dijkstra(start)
# 
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# -------------------------개선된 다익스트라 알고리즘-----------------------------
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    # a ---> b 일때 드는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접노드 확인
        for i in graph[now]:
             cost = dist + i[1]
             # 현재 노드 ---> 다른 노드로 이동하는 거리가 더 짧은 경우
             if cost < distance[i[0]]:
                 distance[i[0]] = cost
                 heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])