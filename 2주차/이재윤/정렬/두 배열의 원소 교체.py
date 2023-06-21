N, K = map(int, input().split())

arr1 = []
arr2 = []

// list(map(int, input().split())으로 입력 받는다
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse=True)

for i in range(K):

    // arr1[i] < arr2[i] 일때만, 입력 받고
    // 아닐 때는 break한다.
    // 왜냐면 최대 K번이기 때문이다  
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(sum(arr1))




