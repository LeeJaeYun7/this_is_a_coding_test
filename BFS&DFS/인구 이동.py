
N, L, R = map(int, input().split())

board = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isInside(x, y):
    if 0<=x and x<N and 0<=y and y<N:
        return True
    else:
        return False

def dfs(x, y, num, check):

    global board
    global L
    global R

    check[x][y] = num

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if isInside(nx,ny) and check[nx][ny] == 0:
            gap = abs(board[x][y] - board[nx][ny])

            if L<= gap and gap <=R:
                dfs(nx, ny, num, check)



day = 0

while True:

    check = [[0]*N for _ in range(N)]
    num = 1

    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                dfs(i, j, num, check)
                num += 1

    totalNums = set()

    for i in range(N):
        for j in range(N):
            totalNums.add(check[i][j])

    if len(totalNums) == N*N:
        break

    populations = dict()
    totalCount = dict()

    for i in range(N):
        for j in range(N):
            num = check[i][j]

            if num in populations:
                totalCount[num] += 1
                populations[num] += board[i][j]
            else:
                totalCount[num] = 1
                populations[num] = board[i][j]

    for i in range(N):
        for j in range(N):
            num = check[i][j]
            population = populations[num]
            count = totalCount[num]
            board[i][j] = population // count


    day += 1


print(day)
