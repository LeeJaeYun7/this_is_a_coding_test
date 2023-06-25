// 변수의 범위 등을 잘 설정해줘야 한다
// N, N-1 등을 명확히 구분해야 한다. 
// 이 문제 같은 경우는 dp[0] 부터 시작해서, dp[N-1]까지의 계산값을 구한다 
// 또한, dp[1]을 max(arr[0], arr[1])로 구해야 한다는 점에 유의해야 한다. 

N = int(input())

arr = list(map(int, input().split()))

dp = [0]*101

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1]) 

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])
    
print(dp[N-1])
