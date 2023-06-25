N, M = map(int, input().split())
INF = 99999999

arr = []
dp = [INF]*10001

for i in range(N):
    num = int(input())
    arr.append(num)
    dp[num] = 1
    
for i in range(1, M+1):
    for j in range(0, N):
        if i - arr[j]>=0:
            dp[i] = min(dp[i], dp[i-arr[j]]+1)
            
if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
