N = int(input())
// 30001만큼 초기화한다 
d = [0]*30001

for i in range(2, N+1):

    // 이렇게 항상 d[i]값을 업데이트 한다 
    d[i] = d[i-1]+1
        
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
 
 
print(d[N]) 
 
