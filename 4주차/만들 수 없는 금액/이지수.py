# import sys
# sys.stdin = open("input1.txt")
#
# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()
#
# for i in range(1, sum(coins)+1):
#     for j in range(n):
#         # 작은 동전부터 더해서 만들어본다
#         if coins[j]