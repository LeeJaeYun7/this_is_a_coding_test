

n = int(input())

board = [] 

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    
dp = [[0]*n for _ in range(n)]

dp[0][0] = board[0][0]


for i in range(1, n):
    
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + board[i][j] 
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + board[i][j]
            
            
maxSum = 0 
for j in range(0, n):
    maxSum = max(maxSum, dp[n-1][j])   
    

print(maxSum)



