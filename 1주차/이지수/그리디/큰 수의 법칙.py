import sys
sys.stdin = open("input1.txt")
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort() # 오름차순으로 정렬
# print(numbers)
result = 0
while True:
    for _ in range(k):
        if m == 0:
            break
        result += numbers[-1]
        m -= 1
    if m == 0: # for문 밖에도 break걸어주는 것이 포인트
        break
    result += numbers[-2]
    m -=1


print(result)