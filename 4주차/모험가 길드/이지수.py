import sys
sys.stdin = open("input1.txt")

n = int(input())
scares = list(map(int, input().split()))
group = []
cnt = 0

# 우선 오름차순으로 정렬
scares.sort(reverse=True)

while scares:
    group.append([scares[0]])