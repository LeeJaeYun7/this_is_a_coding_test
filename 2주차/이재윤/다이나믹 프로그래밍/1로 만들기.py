N = int(input())
// 배열의 초기화는 이렇게 해줄 수 있다 
d = [9999999]*(N+1)
d[1] = 0

for i in range(2, N+1):
        
    if i % 5 == 0:
        // 몫은 //로 써준다 
        // min값을 업데이트 해야 한다. 
        d[i] = min(d[i], d[i//5] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
 
 
    d[i] = min(d[i], d[i-1]+1)
 
print(d[N]) 
