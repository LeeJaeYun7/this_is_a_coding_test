from collections import deque
N, K = map(int, input().split())
is_valid = lambda x, y: 0 <= x < N and 0 <= y < N if True else False

virus_map = []
for i in range(N):
    virus_map.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

virus_dict = {k+1:[] for k in range(K)}
for i in range(N):
    for j in range(N):
        if virus_map[i][j] != 0:
            virus_dict[virus_map[i][j]].append((i, j))

for second in range(S):
    q = deque([])
    for virus_type in virus_dict.keys():
        for element in virus_dict[virus_type]:
            q.append((element, virus_type))
    while q:
        position, virus_type = q.pop()
        x, y = position
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        for i in range(4):
            if is_valid(x+dx[i], y+dy[i]) and virus_map[x+dx[i]][y+dy[i]] == 0:
                virus_map[x+dx[i]][y+dy[i]] = virus_type

print(virus_dict[X-1][Y-1])


