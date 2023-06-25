import random
with open("input.txt", "w") as f:
    for i in range(500):
        f.write(f'{random.randint(0, 100000)}\n')

# with open("dataset_1e5.txt", "w") as f:
#     for i in range(100000):
#         f.write(f'{random.randint(0, 100000000)} ')
#
# with open("dataset_1e6.txt", "w") as f:
#     for i in range(1000000):
#         f.write(f'{random.randint(0, 100000000)} ')
#
# with open("dataset_1e7.txt", "w") as f:
#     for i in range(10000000):
#         f.write(f'{random.randint(0, 100000000)} ')
#
# with open("dataset_1e8.txt", "w") as f:
#     for i in range(100000000):
#         f.write(f'{random.randint(0, 100000000)} ')