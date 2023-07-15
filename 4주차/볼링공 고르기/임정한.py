from collections import Counter
import math
# N, M = list(map(int, input().split()))
# weight = list(map(int, input().split()))
N, M = 8, 5
weight = [1, 5, 4, 3, 2, 4, 5, 2]

weight_cnt = Counter(weight)
total = math.comb(N, 2)
for i, key in enumerate(weight_cnt.items()):
    total-=math.comb(key[1], 2)
print(total)