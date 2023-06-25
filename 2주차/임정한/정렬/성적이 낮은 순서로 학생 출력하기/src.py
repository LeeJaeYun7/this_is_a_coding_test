from typing import List

n = int(input())
scoreboard = {}

for i in range(n):
    name, score = input().split()
    scoreboard[name] = int(score)

result = sorted(scoreboard.items(), key=lambda x:-x[1])
# print(sorted(scoreboard.items(), key=lambda x:(-x[1], x[0])))

for i in result:
    print(i[0], end=' ')