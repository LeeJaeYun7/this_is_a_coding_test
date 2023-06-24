import sys
sys.stdin = open("input3.txt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a는 오름차순
b.sort(reverse=True) # b는 내림차순

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
print(sum(a))