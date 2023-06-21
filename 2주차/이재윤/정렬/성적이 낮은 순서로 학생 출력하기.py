N = int(input())

array = []

for i in range(N):
    // input.split()으로 입력 받는다
    input_data = input().split()
    name = input_data[0]
    point = int(input_data[1])
    // array.append((name,point))로 더해준다. 
    array.append((name, point))

// 람다 함수를 활용해서 student[1]로 정렬해준다. 
array = sorted(array, key=lambda student:student[1])

// array를 순회하면서, data[0]을 출력한다. 
for data in array:
    print(data[0], end=' ')
