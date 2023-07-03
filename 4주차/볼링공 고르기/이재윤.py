// 2개의 조합을 구하는 케이스를 2중 for문으로 구하면 된다


N, M = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0 

for i in range(0, N):
    for j in range(i+1, N):
        if arr[i] != arr[j]:
            ans += 1
            
print(ans)
