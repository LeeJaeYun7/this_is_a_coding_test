coins = [500, 100, 50, 10]
ans = 0 

N = int(input())

for coin in coins:
    ans += N//coin
    N %= coin
    
print(ans)
    
    
