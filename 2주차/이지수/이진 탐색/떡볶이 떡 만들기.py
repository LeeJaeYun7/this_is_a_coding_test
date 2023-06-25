import sys
sys.stdin = open("input2.txt")

n, m = map(int, input().split())
tteoks = list(map(int, input().split()))

# 가장 긴 떡의 길이만큼 높이 설정 가능
start = 0
end = max(tteoks)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 # 절단기 높이
    for tteok in tteoks:
        # 잘랐을 때의 떡의 양 계산
        if tteok > mid: # 떡이 절단기보다 길면
            total += tteok - mid # 잘려서 total에 더해진다
    if total < m: # total이 target보다 작으면
        end = mid - 1 # 더 많이 자르기 => 왼쪽 탐색
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result 기록!! 이 포인트.
        start = mid + 1 # start 바꿔주기

print(result)

