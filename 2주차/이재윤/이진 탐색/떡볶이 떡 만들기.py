
def binary_search(N, M, array):
    
    start = 0
    end = max(array)
    ans = 0 
    
    while start<=end:
        
        mid = (start+end)// 2
        sum = 0
        
        for i in array:
            if i >= mid:
                sum += (i-mid)
                
        if sum >= M:
            ans = mid
            start = mid+1
        else:
            end = mid-1 
            
    
    return ans 
        
    
    
N, M = map(int, input().split())

array = list(map(int, input().split()))

maxHeight = binary_search(N, M, array)

print(maxHeight) 




