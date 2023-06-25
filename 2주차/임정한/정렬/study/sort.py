import time

lst = []
with open("dataset_1e7.txt") as f:
    lst = f.readline().split()

class SortingAlgorithm:
    def __init__(self):
        self.data = lst
        print("processing finished")

    def quick(self):
        def _quick(lst):
            if len(lst)<=1:
                return lst
            pivot, lst = lst[0], lst[1:]

            return _quick([x for x in lst if x<=pivot])+[pivot]+_quick([x for x in lst if x>pivot])

        s_t = time.time()
        _quick(self.data)
        print(time.time()-s_t)

    def merge(self):
        pass

    def count(self):
        pass

algorithm = SortingAlgorithm()
algorithm.quick()