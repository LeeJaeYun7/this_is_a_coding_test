import sys
sys.stdin = open("input2.txt")

n = int(input())
scores = []
for _ in range(n):
    a, b = map(str, input().split())
    scores.append((int(b), a))

scores.sort(reverse=True)
for i in range(n):
    print(scores[i][1], end=' ')