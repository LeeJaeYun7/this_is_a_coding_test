from collections import Counter


def solution(food_times, k):
    answer = 0
    iteration = 0
    counter_times = Counter(food_times)
    kprime = k
    while True:
        for i, key in enumerate(counter_times.items()):
            if key[1] != 0:
                k -= 1
        if k <= -1:
            break
        iteration += 1
        kprime = k
    food_times = [max(food_times[i] - iteration, 0) for i in range(len(food_times))]
    print(food_times, kprime)
    if sum(food_times) == 0:
        return -1

    while True:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                kprime -= 1
            if kprime == -1:
                return i + 1

#시간초과 및 정확성 미달