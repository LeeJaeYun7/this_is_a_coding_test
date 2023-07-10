def solution(s):
    answer = 0
    
    total = len(s)
    minLen = 999999999
    
    for i in range(1, total+1):
        ans = ''
        start = 0
        end = i
        strList = []
        
        while True:
            if start>=len(s):
                break
            
            if end>len(s):
                end = len(s) 
            
            tmp = s[start:end]
            strList.append(tmp)
            start += i
            end += i
        
        cnt = 1
        
        for j in range(1, len(strList)):
            if strList[j-1] == strList[j]:
                cnt += 1
            else:
                if cnt != 1:
                    ans += str(cnt)
                    cnt = 1
                ans += strList[j-1]
        
        if cnt != 1:
            ans += str(cnt)
        ans += strList[len(strList)-1]
                
        minLen = min(minLen, len(ans))        
        
        
        
    answer = minLen    
        
    return answer
