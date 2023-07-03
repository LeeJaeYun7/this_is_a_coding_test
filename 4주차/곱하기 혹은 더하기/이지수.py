import sys
sys.stdin = open("input2.txt")
s = input()
result = 1

for i in range(len(s)):
    if s[i] == '0':
        continue
    elif i != 0 and s[i-1] == '0':
        result += int(s[i]) - 1
    elif i != 0 and s[i-1] == '1':
        result += int(s[i])
    else:
        result *= int(s[i])
# if s[-1] != '0':
#     result *= int(s[-1])
print(result)

# 문자열을 돌면서 0이면 더하기, 0이 아니면 곱하기를 해준다.
# 0뿐만 아니라 1일때를 간과했다! 1이 나오면 곱할 때보다 더할 때 더 큰 수를 만들 수 있다.