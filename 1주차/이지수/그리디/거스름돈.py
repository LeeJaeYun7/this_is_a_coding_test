coins = [500, 100, 50, 10] # 동전 담기
n = int(input()) # 거슬러줘야 하는 돈 N
ans = 0 # 동전 개수
for coin in coins:
    ans += n//coin
    n %= coin

print(ans)