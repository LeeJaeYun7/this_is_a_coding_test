def factorial_itertive(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    return n * factorial_recursive(n-1)

# 5! 출력
print('반복적으로 구현: ', factorial_itertive(5))
print('재귀적으로 구현: ', factorial_recursive(5))