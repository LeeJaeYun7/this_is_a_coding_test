import sys
sys.stdin = open('input1.txt')

n = int(input())
direction = list(map(str, input().split())) # 이동방향
arr = [[] for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i-1].append((i, j)) # 좌표 입력
start = [0, 0] # 시작좌표
for i in range(len(direction)):
    if direction[i] == 'R' and start[1] + 1 < n: # 우 + 좌표가 범위 안에 있을 때
            start[1] += 1
    elif direction[i] == 'U' and start[0] - 1 >= 0: # 위
        start[0] -= 1
    elif direction[i] == 'D' and start[0] + 1 < n: # 아래
        start[0] += 1
    elif direction[i] == 'L' and start[1] - 1 >= 0: # 왼
        start[1] -= 1
print(*arr[start[0]][start[1]])

# ------------------------- 리팩토링 (책 코드 참고) ---------
# n = int(input())
# x, y = 1, 1 # 시작 좌표
# directions = input().split()
# move_types = ['L', 'R', 'U', 'D']
#
# dx = [0, 0, -1, 1] # 하 상 좌 우
# dy = [-1, 1, 0, 0]
#
# for direction in directions:
#     for i in range(4):
#         if direction == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny