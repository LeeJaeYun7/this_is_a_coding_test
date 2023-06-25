lst = [1, 4, 3, 2, 5, 6, 7, 3]

lst2 = lst.copy()
lst2.sort()
print(lst2)

lst3 = lst.copy()
lst3.sort(key=lambda x: -x)
print(lst3)

lst4 = lst.copy()
print(sorted(lst4))

dictionary = {1: 7, 2: 6, 3: 5, 4: 4}

dictionary2 = dictionary.copy()
print(sorted(dictionary2.items(), key=lambda x: x[0]))


def value_getter(item):
    return item[1]


print(sorted(dictionary2.items(), key=value_getter))

for i in reversed(dictionary2):
    print(dictionary2[i])
