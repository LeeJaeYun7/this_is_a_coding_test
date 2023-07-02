# N = int(input())
# x = list(map(int, input().split()))

def solution1(n, x):
    x.sort(reverse=True)
    cnt = 0
    while x:
        cnt+=1
        element = x[0]
        if len(x)>element:
            x = x[element:]
        else:
            break
    return cnt

def solution2(n, x):
    x.sort(reverse=True)
    cnt, pnt, N = 0, 0, len(x)
    while N:
        cnt+=1
        if N>x[pnt]:
            N-=x[pnt]
        else:
            break
        pnt+=1
    return cnt

def solution3(N, x):
    x.sort(reverse=True)
    cnt = 0
    pnt = 0
    while pnt<N:
        cnt+=1
        pnt+=x[pnt]
    return cnt


def test_1():
    N = 20
    inp = [6, 4, 3, 3, 7, 8, 9, 6, 5, 4, 5, 7, 7, 5, 4, 3, 2, 4, 5, 6]
    assert solution3(N, inp) == 4

test_1()