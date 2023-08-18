

T = int(input())


for i in range(T):
    
    
    board = [] 
    n, m = map(int, input().split())
    row = list(map(int, input().split()))
    
    pos = 0
    
    for j in range(n):
        tmp = [] 
        
        for k in range(m):
            num = row[pos]
            tmp.append(num)
            pos += 1 
            
        board.append(tmp)
        
    dp = [[0]*m for _ in range(n)]

    for j in range(n):
        dp[j][0] = board[j][0] 
    
    
    
    for k in range(1, m):
    
        for j in range(0, n):
            if j == 0:
                dp[j][k] = max(dp[j][k-1], dp[j+1][k-1]) + board[j][k]
            elif j == n-1:
                dp[j][k] = max(dp[j-1][k-1], dp[j][k-1]) + board[j][k]
            else:
                dp[j][k] = max(dp[j-1][k-1], dp[j][k-1], dp[j+1][k-1]) + board[j][k] 
            
            
    maxSum = 0         
        
    for k in range(n):
        maxSum = max(maxSum, dp[k][m-1])
                
    print(maxSum)
            
            
