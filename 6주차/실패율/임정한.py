from collections import Counter


def solution(N, stages):
    user = len(stages)
    failure_rate = {}
    counter = Counter(stages)
    for i in range(N):
        try:
            failure_rate[i + 1] = counter[i + 1] / user
            user -= counter[i + 1]
        except:
            failure_rate[i + 1] = 0

    failure_rate = {k: v for k, v in sorted(failure_rate.items(), key=lambda x: (-x[1]))}
    return list(failure_rate.keys())
