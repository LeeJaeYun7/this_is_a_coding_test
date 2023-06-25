// 문제에서의 제약 조건에 반드시 유의해야 한다 

N = int(input())
dp = [0]*1001

dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1]+2*dp[i-2]) % 796796
    
print(dp[N])
