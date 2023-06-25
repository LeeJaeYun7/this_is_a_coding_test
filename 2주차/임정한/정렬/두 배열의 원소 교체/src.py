N, M = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort(reverse=True)

for i in range(M):
    A[i] = max(A[i], B[i])

print(sum(A))