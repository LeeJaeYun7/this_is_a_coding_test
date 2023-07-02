N = int(input())

arr = list(map(int, input().split()))

arr.sort()
ans = 0 

pos = 0
tmp = []

while pos<N:
    
    num = arr[pos]
    tmp.append(num)
    
    if max(tmp) == len(tmp):
        ans += 1
        tmp = [] 
    
    pos += 1
    
    
print(ans)
