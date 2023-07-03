// 다양한 케이스를 고려하여 문제를 풀도록 하자 

string = input()

sum = 0

for c in string:
    num = int(c)
    
    if num == 0 or num == 1 or sum <=1:
        sum += num
    else:
        sum *= num


print(sum)
