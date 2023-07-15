def solution(s: str):
    if len(s) == 1:
        return int(s)

    return max(solution(s[:-1])*int(s[-1]), solution(s[:-1])+int(s[-1]))


def test_case1():
    example = "02984"
    assert solution(example) == 576


def test_case2():
    example = "567"
    assert solution(example) == 210


def test_case3():
    example = "1"
    assert solution(example) == 1


def test_case4():
    example = "12345678901234567890"
    assert solution(example) == (((1+2)*3*4*5*6*7*8*9)+1)*2*3*4*5*6*7*8*9


if __name__ == "__main__":
    # s = input()
    # print(solution(s))

    test_case1()
    test_case2()
    test_case3()
    test_case4()