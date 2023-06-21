import sys
sys.stdin = open('input1.txt')

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True) # 내림차순으로 정렬

for number in numbers:
    print(number, end=' ')