N = int(input())
array = []

for i in range(N):
    num = int(input())
    array.append(num)

// sorted와 reverse=True를 이용해서 내림차순 정렬을 한다 
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
