# Result :Wrong
# 5^10+1 운 1을 빼고 5로 나누는 경우가 2로 나는 경우보다 나음.

memo= {}

x = int(input())

divisors = [5, 3, 2]
cnt = 0
flag = False
while True:
    if x == 1:
        break
    cnt += 1
    for divisor in divisors:
        if not x%divisor:
            x = x //divisor
            flag= True
            continue
    if flag:
        flag = False
        continue
    x-=1
    print(x)


print(cnt)