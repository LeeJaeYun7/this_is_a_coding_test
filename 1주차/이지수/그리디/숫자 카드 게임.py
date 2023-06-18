import sys
sys.stdin = open("input2.txt")

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
# cards.sort()
answer = []

for i in range(n):
    answer.append(min(cards[i]))
print(max(answer))

# 이차원 그래프로 입력받고 행별로 오름차순 sort했다. - 이제보니 필요 없음

# -------------------------------책 풀이
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
# print(result)

# 한 줄씩 입력받아 그때그때 최솟값을 바꿔 나가는 방식.