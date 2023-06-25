N, M = map(int, input().split())
lst = list(map(int, input().split()))
MAX_VALUE = 99999
table = [MAX_VALUE for i in range(10001)]

for element in lst:
    table[element] = 1

for i in range(M+1):
    if i <min(lst):
        continue
    for element in lst:
        table[i] = min(table[i-element]+1, table[i])

if table[M] == MAX_VALUE:
    print(-1)
else:
    print(table[M])