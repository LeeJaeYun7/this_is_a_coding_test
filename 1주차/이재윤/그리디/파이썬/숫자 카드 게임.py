n, m = map(int, input().split())

maxNum = 0 

for i in range(0, n):
    data = list(map(int, input().split()))
    maxNum = max(maxNum, min(data))
    
print(maxNum)
