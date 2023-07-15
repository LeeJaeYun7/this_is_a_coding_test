def solution(s: str):
    cnt = 0
    flag = s[0]
    for i in range(len(s)):
        if flag != s[i]:
            cnt+=1
            flag = s[i]
    return (cnt+1)//2

def test_case1():
    x = "0001100"
    assert solution(x) == 1

def test_case2():
    x = "00011"
    assert solution(x) == 1

def test_case3():
    x = "00011001"
    assert solution(x) == 2

def test_case4():
    x = "0"
    assert solution(x) == 0

def test_case5():
    x = "0001100101"
    assert solution(x) == 3

def backjoon_testcase():
    xs = ["11001100110011000001", "11101101", "00000001"]
    ys = [4, 2, 1]
    for i, x in enumerate(xs):
        assert solution(x) == ys[i]


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    backjoon_testcase()