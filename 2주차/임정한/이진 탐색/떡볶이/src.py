N, M = map(int, input().split())
data = list(map(int, input().split()))

def left_sum(criteria):
    left = [max(0, data[i]-criteria) for i in range(N)]
    return sum(left)

start = max(data)
end = 0
while start>=end:
    print(start, end)
    mid = (start+end)//2
    if left_sum(mid) > M:
        end = mid
    elif left_sum(mid)<M:
        start = mid-1
    if start == end or start-1 == end:
        print(start)
        break

