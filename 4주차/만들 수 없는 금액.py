// 풀이를 참고했다
// 나중에 한 번 다시 풀어보자 

N = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1

for i in coin:
    if i > target:
        break
    target += i

print(target)
