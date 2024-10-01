N = int(input())
K = int(input())

apples = []
snake = [[0, 0]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def isInside(x, y):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    else:
        return False

for i in range(K):
    r, c = map(int, input().split())
    apples.append([r-1, c-1])

L = int(input())

directionInfo = []

for i in range(L):
    time, dir = map(str, input().split())
    directionInfo.append([int(time), dir])

currTime = 1
dir = 0

while True:

    x, y = snake[0]

    nx = x + dx[dir]
    ny = y + dy[dir]

    if not isInside(nx, ny) or [nx,ny] in snake:
        break

    snake.insert(0, [nx, ny])

    if [nx,ny] in apples:
        apples.remove([nx,ny])
    else:
        snake.pop()

    directionChanged = False

    for time, turn in directionInfo:
        if currTime == time:
            if turn == "L":
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1
            else:
                if dir == 3:
                    dir = 0
                else:
                    dir += 1

            directionChanged = True
            break

    if directionChanged == True:
        directionInfo.pop(0)

    currTime += 1


print(currTime)
