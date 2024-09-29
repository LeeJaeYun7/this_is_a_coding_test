N = int(input())

board = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0]*N for _ in range(N)]

dp[0][0] = board[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + board[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+board[i][j], dp[i-1][j] + board[i][j])

maxResult = -1e9
for j in range(0, N):
    maxResult = max(maxResult, dp[N-1][j])

print(maxResult)
