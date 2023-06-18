import sys
sys.stdin = open('input2.txt')

n = int(input())
cnt = 0 # 3이 포함된 시각을 세어 담는 변수

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                cnt += 1

print(cnt)