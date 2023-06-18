import sys
sys.stdin = open('input1.txt')
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(a, b):
    flag = False
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = 1 #방문체크
                q.append((nx, ny))
                flag = True
    return flag



n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1
print(result)

# DFS 풀이
# n, m = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(n)]
#
# def dfs(x, y):
#     # 범위 밖이면 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if arr[x][y] == 0:
#         arr[x][y] = 1 # 방문처리
#         # 상 하 좌 우 위치 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
# print(result)