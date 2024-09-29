from collections import deque

N, K = map(int, input().split())

board = [[0]*N for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(N):
        board[i][j] = row[j]

S, X, Y = map(int, input().split())

viruses = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        num = board[i][j]
        if num != 0:
            viruses[num].append([i, j])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isInside(x, y):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    else:
        return False

time = 0

def isFull(board):

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return False

    return True

while True:

    if time == S:
        break
    
    for i in range(1, K+1):
        virus = viruses[i]
        newVirus = []

        for x, y in virus:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if isInside(nx, ny) and board[nx][ny] == 0:
                    board[nx][ny] = i
                    newVirus.append([nx,ny])

        viruses[i] = newVirus

    time += 1
    if isFull(board):
        break


print(board[X-1][Y-1])
