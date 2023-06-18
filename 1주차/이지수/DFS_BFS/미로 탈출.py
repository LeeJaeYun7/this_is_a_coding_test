import sys
sys.stdin = open('input2.txt')
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
    return arr[n-1][m-1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)] # 미로
print(bfs(0, 0))
