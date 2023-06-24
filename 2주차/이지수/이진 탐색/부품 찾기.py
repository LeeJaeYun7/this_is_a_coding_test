import sys
sys.stdin = open("input1.txt")

n = int(input())
stock = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

stock.sort()

def binary_search(s, e, target, array):
    while s <= e:
        mid = (s+e) // 2
        if target == array[mid]:
            return True
        elif target > array[mid]:
            s = mid + 1
        elif target < array[mid]:
            e = mid - 1
    return False


start = 0
end = n-1
for i in range(m):
    result = binary_search(start, end, find[i], stock)
    if result == True:
        print("yes", end=' ')
    else:
        print("no", end=' ')
