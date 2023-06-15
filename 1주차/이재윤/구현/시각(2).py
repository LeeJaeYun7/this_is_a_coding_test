N = int(input())

ans = 0 

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                ans += 1
        
print(ans)
