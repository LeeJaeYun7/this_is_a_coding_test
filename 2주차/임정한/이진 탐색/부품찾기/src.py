import time

src, dst = None, None

with open("dataset_1e6.txt") as f:
    src= f.readline()
with open("dataset_1e5.txt") as f:
    dst= f.readline()

N = 100000
M = 10000

def first_solution(src, dst):
    from collections import Counter
    s_t = time.time()
    src = list(map(int, src.split()))
    dst = list(map(int, dst.split()))
    src = Counter(src)
    # print(src)
    for ele in dst:
        if src[ele]:
            print("yes", end=" ")
        print("no", end=" ")

    print(time.time()-s_t) # 0.43sec

def second_solution(src, dst): # FIXME : TOO LONG
    def binary_search(lst, target, threshold=6) -> bool:
        """
        :param lst: data
        :param target: data to find
        :param scope: [x, y)
        :return: (bool) existence
        """
        # print(f'{lst}, {target}')
        N = len(lst)
        if N <= threshold:
            if target in lst:
                return True
            return False
        pivot = lst[N//2]
        if target<=pivot:
            return binary_search(lst[0:N // 2], target, threshold)

        return binary_search(lst[N//2:N], target, threshold)


    s_t = time.time()
    src = list(map(int, src.split()))
    dst = list(map(int, dst.split()))

    src.sort()

    for i, ele in enumerate(dst):
        print(binary_search(src, ele, 6), i)
    print(time.time() - s_t)  # 0.26sec


first_solution(src, dst)
# second_solution(src, dst)
