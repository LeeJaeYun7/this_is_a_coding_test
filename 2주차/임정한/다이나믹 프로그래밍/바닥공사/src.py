n = int(input())

table = [0 for i in range(1001)]
table[1] = 1
table[2] = 3
for i in range(3, n+1):
    table[i] = table[i-1] + 2*table[i-2]

print(table[n] % 796796)