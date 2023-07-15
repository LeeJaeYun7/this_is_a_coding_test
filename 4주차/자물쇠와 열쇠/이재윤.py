// 문제의 조건을 꼼꼼히 읽는 것은 기본이다
// 코드의 효율성을 개선해야 한다 

def changeDir(key, M):
    
    tmpKey = [[0]*M for _ in range(M)]
    
    for i in range(M):
        for j in range(M):
            tmpKey[j][(M-1)-i] = key[i][j]
    
    for i in range(M):
        for j in range(M):
            key[i][j] = tmpKey[i][j]
            
    
def putKey(keyBoard, sx, sy, key):
    
    M = len(key)
    
    for i in range(sx, sx+M):
        for j in range(sy, sy+M):
            keyBoard[i][j] = key[i-sx][j-sy]
            
            
def isOpen(board, keyBoard, N):
    
    open = True
    
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            if board[i][j] == 1 and keyBoard[i][j] == 1:
                open = False
            elif board[i][j] == 1 and keyBoard[i][j] == 0:
                continue
            elif board[i][j] == 0 and keyBoard[i][j] == 1:
                continue
            elif board[i][j] == 0 and keyBoard[i][j] == 0:
                open = False 
                
    return open 
    


def solution(key, lock):
    answer = False
    
    N = len(lock)
    M = len(key)
    board = [[0]*(3*N) for _ in range(3*N)]

    for i in range(N, 2*N):
        for j in range(N, 2*N):
            board[i][j] = lock[i-N][j-N]
            
    for i in range(0, 3*N-M+1):
        for j in range(0, 3*N-M+1):
            for k in range(4):
                keyBoard =[[0]*(3*N) for _ in range(3*N)]
                putKey(keyBoard, i, j, key)
                changeDir(key, M)
            
                res = isOpen(board, keyBoard, N)
                
                if res == True:
                    answer = True
            
    return answer
    
