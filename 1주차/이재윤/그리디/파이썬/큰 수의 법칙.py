n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
dataLen = len(data)
ans = 0 
cnt = 0 

for i in range(0, m):
    if cnt == k:
        ans += data[1]
        cnt = 0
    else:
        ans += data[0]
        cnt += 1
        
print(ans)
