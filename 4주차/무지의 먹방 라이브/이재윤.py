// 시간 초과 및 정확성 오류  

import heapq


def solution(food_times, k):
    
    answer = -1 
    
    pq = []
    check = [False]*200010 
    total = 0
    stage = 0 
    foodLen = len(food_times)
    initFoodLen = foodLen
    
    for i in range(0, len(food_times)):
        heapq.heappush(pq, (food_times[i], i))
    
    
    while pq: 
    
        num, pos = heapq.heappop(pq)
        num -= stage 
        
        if total + foodLen*num < k:
            total += foodLen*num
            foodLen -= 1 
            stage += num 
            check[pos] = True 
        else:
            cnt = 0 
            
            for i in range (0, initFoodLen):
                if check[i] == False:
                    cnt += 1 
                if total+cnt == k:
                    answer = i
                    break 
            
            answer += 1
            answer %= initFoodLen
            
            while True: 
                if check[answer] == False:
                    break
                else:
                    answer += 1 
                    answer %= initFoodLen
                    
            answer += 1 
        
        if answer != -1:
            break
        
    
    
    return answer
