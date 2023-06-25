import sys

sys.stdin = open("input.txt")
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort(key=lambda x: -x)

for i in range(n):
    print(lst[i], end=' ')