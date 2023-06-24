def binary_search(array, target, start, end):
    # array : 찾을 범위 / target: 찾을 값 / start: 시작점 / end: 끝점
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    # 중간점 값보다 찾을 값이 작으면 왼쪽만 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점 값보다 찾을 값이 크면 오른쪽 확인 => 중간점보다 하나 큰 값이 시작점
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("찾을 원소가 존재하지 않습니다.")
else:
    print(result+1)

# ------------반복문으로 구현-------------------

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         elif array[mid] < target:
#             start = mid + 1
#     return None