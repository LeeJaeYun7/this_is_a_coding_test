// 음수를 나눌 때의 케이스를 잘 고려해야 한다 

N = int(input())

arr = list(map(int, input().split()))

symbols = list(map(int, input().split()))
maxRes = -int(1e9)
minRes = int(1e9)

def dfs(pos, res, selected):
    
    global minRes
    global maxRes
    
    if pos == N:
        minRes = min(minRes, res)
        maxRes = max(maxRes, res)
        return 
    
    
    for i in range(4):
        if symbols[i] == 0:
            continue
        
        tmp = 0 
        
        if i == 0:
            selected.append('+')
            res += arr[pos]        
        elif i == 1:
            selected.append('-')
            res -= arr[pos]
        elif i == 2:
            selected.append('*')
            res *= arr[pos]
        elif i == 3: 
            selected.append('/')
            if res < 0:
                tmp = -res // arr[pos]
                tmp *= (-1)
            else:
                tmp = res // arr[pos]
            res = tmp 
            
        symbols[i] -= 1
        dfs(pos+1, res, selected)
        symbols[i] += 1 
        selected.pop(len(selected)-1)
    
        if i == 0:
            res -= arr[pos]        
        elif i == 1:
            res += arr[pos]
        elif i == 2:
            res = res // arr[pos]
        elif i == 3: 
            res = res*tmp


selected = [] 
dfs(1, arr[0], selected)
print(maxRes)
print(minRes)





