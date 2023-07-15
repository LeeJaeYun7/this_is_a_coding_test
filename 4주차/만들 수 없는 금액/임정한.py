def solution(N, coin_type):
    cost = []
    coin_type.sort()
    for i in range(N):
        for j in range(len(cost)):
            cost.append(cost[j]+coin_type[i])
        cost.append(coin_type[i])
    cnt = 1
    while True:
        if cnt not in cost:
            return cnt
        cnt+=1

def test_solution():
    Ns = [5, 3]
    coin_types = [[3,2, 1, 1, 9], [3, 5, 7]]
    result = [8, 1]
    for i in range(len(Ns)):
        assert solution(Ns[i], coin_types[i]) == result[i]


if __name__ == "__main__":
    # N = int(input())
    # coin_type = list(map(int, input().split()))
    # print(solution(N, coin_type))

    test_solution()