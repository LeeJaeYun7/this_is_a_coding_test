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
    for virus_type in virus_dict.keys():
        virus_dict[virus_type]


bfs(starting)
