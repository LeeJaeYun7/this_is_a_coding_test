N = int(input())
array = []

for i in range(N):
    num = int(input())
    array.append(num)
    
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
