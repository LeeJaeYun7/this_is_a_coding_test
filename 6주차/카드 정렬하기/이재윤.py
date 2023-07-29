// 우선순위 큐를 사용하는 것이 핵심인 문제이다 
// 단, N=1일때는 비교가 일어나지 않으므로, 이 케이스를 고려해야 한다 

import heapq

hq = []
arr = [] 
N = int(input())

for i in range(N):
    num = int(input())
    arr.append(num)

ans = 0 

for i in range(0, len(arr)):
    heapq.heappush(hq, arr[i])

if N >= 2:    
    while True:
    
        num1 = heapq.heappop(hq)
        num2 = heapq.heappop(hq)
    
        ans += (num1+num2)
        if len(hq) == 0:
            break 
    
        heapq.heappush(hq, num1+num2)
    
print(ans)
    
