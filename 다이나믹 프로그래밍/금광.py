T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    board = [[0]*m for _ in range(n)]

    tmpList = list(map(int, input().split()))
    pos = 0

    for j in range(n):
        for k in range(m):
            board[j][k] = tmpList[pos]
            pos += 1

    dp = [[0]*m for _ in range(n)]

    for j in range(n):
        dp[j][0] = board[j][0]

    for k in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][k] = max(dp[j][k-1]+board[j][k], dp[j+1][k-1]+board[j][k])
            elif j == n-1:
                dp[j][k] = max(dp[j][k-1]+board[j][k], dp[j-1][k-1]+board[j][k])
            else:
                dp[j][k] = max(dp[j-1][k-1]+board[j][k], dp[j][k-1]+board[j][k], dp[j+1][k-1]+board[j][k])

    maxResult = 0

    for j in range(n):
        maxResult = max(maxResult, dp[j][m-1])

    print(maxResult)
