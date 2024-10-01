answer = False
N = int(input())
board = []
teachers = []
isCatched = False

def isInside(x, y):
    if 0<=x and x < N and 0<=y and y<N:
        return True
    else:
        return False

for i in range(N):
    row = list(map(str, input().split()))
    board.append(row)

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append([i,j])

def moveTeacher(x, y, dir):

    global isCatched

    if not isInside(x, y):
        return

    if board[x][y] == 'O':
        return

    if board[x][y] == 'S':
        isCatched = True
        return

    if dir == 0:
        moveTeacher(x-1, y ,dir)
    elif dir == 1:
        moveTeacher(x+1, y, dir)
    elif dir == 2:
        moveTeacher(x, y-1, dir)
    elif dir == 3:
        moveTeacher(x, y+1, dir)



def findStudents():

    global N
    global board
    global isCatched

    isCatched = False

    for teacher in teachers:
        x = teacher[0]
        y = teacher[1]

        for i in range(4):
            moveTeacher(x, y, i)


def dfs(cnt):

    global answer

    if cnt == 3:
        findStudents()

        if isCatched == False:
            answer = True

        return

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(cnt+1)
                board[i][j] = 'X'


dfs(0)
if answer == True:
    print("YES")
else:
    print("NO")



