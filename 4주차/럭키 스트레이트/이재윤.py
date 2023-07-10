name = input()

sum1 = 0
sum2 = 0

for i in range(0, len(name)//2):
    sum1 += int(name[i])
    
for i in range(len(name)//2, len(name)):
    sum2 += int(name[i])
    
    
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
    
