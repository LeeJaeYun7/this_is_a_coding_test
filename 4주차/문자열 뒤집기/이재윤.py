string = input()

sum = 0
zeroCnt = 0
oneCnt = 0 

if string[0] == '0':
    curr = '0'
    zeroCnt += 1
else:
    curr = '1'
    oneCnt += 1

for i in range(1, len(string)):
    if curr == string[i]:
        continue
    else:
        if curr == '0':
            curr = '1'
            oneCnt += 1
        else:
            curr = '0'
            zeroCnt += 1

print(min(zeroCnt, oneCnt))
    

