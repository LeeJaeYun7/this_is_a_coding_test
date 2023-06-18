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