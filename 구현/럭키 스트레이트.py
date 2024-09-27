num = int(input())

strNum = str(num)

totalLen = len(strNum)
left = 0 
right = 0 
for i in range(0, totalLen // 2):
    left += int(strNum[i])
    
for i in range(totalLen // 2, totalLen):
    right += int(strNum[i])
    
if left == right:
    print("LUCKY")
else:
    print("READY")
    
    
