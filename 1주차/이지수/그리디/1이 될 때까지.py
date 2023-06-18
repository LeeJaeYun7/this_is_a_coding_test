import sys
sys.stdin = open("input3.txt")

n, k = map(int, input().split())

cnt = 0 # 연산 횟수를 저장하는 변수
while True:
    if n == 1: # N이 1이 되면 연산을 멈추고 cnt를 반환
        print(cnt)
        break
    if n%k == 0: # 나누어 떨어지면 무조건 나눠준다.
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

# ----------------------책의 풀이
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     target = (n // k) * k
#     result += (n - target) # k의 배수가 될 때까지 한번에 빼서 저장,,!
#     n = target
#     if n < k:
#         break
#     result += 1
#     n //= k
# result += (n - 1)
# print(result)

# N의 범위가 10만 이하 => 일일이 1씩 빼도 해결할 수 있지만
# N이 100억 이상 => n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 코드를 작성할 수 있다.