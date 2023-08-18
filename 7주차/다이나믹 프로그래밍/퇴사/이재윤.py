
N = int(input())

T = []
P = []

T.append(0)
P.append(0)
maxSum = 0 

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
    
def dfs(day, sum, last):
    
    global maxSum 
    
    if day >= N+1:
        
        if day == N+1:
            maxSum = max(maxSum, sum)
        else:
            maxSum = max(maxSum, sum-last)
        return 
    
    
    dfs(day+T[day], sum+P[day], P[day])
    dfs(day+1, sum, 0)
  

dfs(1, 0, 0)
    
print(maxSum)
    
