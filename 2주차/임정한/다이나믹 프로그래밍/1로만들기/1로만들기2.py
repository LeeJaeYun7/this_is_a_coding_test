x = int(input())
# x = 5*5*5*5*5+1
d = [0]*30001

divisors = [2, 3, 5]
for i in range(2, x+1):
    d[i] = d[i-1]+1
    for divisor in divisors:
        if not i%divisor:
            d[i] = min(d[i], d[i//divisor]+1)
print(d[x])