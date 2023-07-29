// 도달 인원이 0일때를 잘 고려해야 한다 

def solution(N, stages):
    ans = []
    answer = []
    total = len(stages)
    initTotal = total 
    
    stage = 1
    selected = [False]*total 
    
    while True:
        
        if stage == N+1:
            break 
        
        cnt = 0 
        for i in range(0, initTotal):
            if (selected[i] == False) and (stages[i] <= stage):
                selected[i] = True 
                cnt += 1 
        if total != 0:        
            ans.append((stage, cnt/total))
        else:
            ans.append((stage, 0))
        total -= cnt 
        stage += 1 
        
    ans.sort(key=lambda x : -x[1])
    
    for i in range(0, len(ans)):
        answer.append(ans[i][0])
    
    return answer
