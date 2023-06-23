def binary_search(N, target, array):
    
    start = 0 
    end = N-1
    
    while start<=end:
        
        mid = (start+end) // 2
        
        if array[mid] == target:
            return "YES"
        elif array[mid] < target:
            start = mid+1
        elif array[mid] > target:
            end = mid-1
            
    
    return "NO"
    
    
N = int(input())
array = list(map(int, input().split()))
array.sort() 

M = int(input())
requests = list(map(int, input().split()))


for request in requests:
    res = binary_search(N, request, array)
    print(res, end=' ')



