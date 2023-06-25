N = int(input())
data = list(map(int, input().split()))

table = [0 for i in range(100)]


def sum(n: int):
    if n == 0:
        return data[0]
    if n == 1:
        return max(data[0], data[1])
    return max(sum(n-2)+data[n], sum(n-1))

table[0], table[1] = data[0], max(data[0], data[1])
for i in range(2, N):
    table[i] = max(table[i-2]+data[i], table[i-1])

print(table[N-1])
print(sum(N-1))