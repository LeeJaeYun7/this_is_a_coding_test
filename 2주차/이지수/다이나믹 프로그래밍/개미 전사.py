import sys
sys.stdin = open("input1.txt")
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

# 피보나치 수열처럼 풀면 된다 !!!!
d[0] = array[0]
d[1] = array[1]
for i in range(2, n):
    # 현재 식량창고보다 하나 전 거 털때 / 현재 식량창고 + 전전 식량창고 털 때 더한거랑 비교
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])