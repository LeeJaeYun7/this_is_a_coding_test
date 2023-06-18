import sys
sys.stdin = open('input4.txt')
# 백준 로봇청소기같은 문제

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

visited[x][y] = 1 # 출발지점 방문 체크
cnt = 0

dx = [-1, 0, 0, -1]
dy = [1, 0, -1, 0]

while True:
    flag = 0
    for _ in range(4): # 4방향으로 돌린다
        d = (d+3)%4
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 안이고, 방문한 적 없고, 바다가 아니라면
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x = nx
                y = ny
                flag = 1
                break
    if flag == 0:
        if arr[x-dx[d]][y-dy[d]] == 1:
            break
        else: # 뒤로 갈 수 있다면
            x, y = x-dx[d], y-dy[d]


print(cnt)