import sys
sys.stdin = open('input3.txt')

n = input() # 체스말의 위치 입력
x = ord(n[0])-97 # 아스키코드를 이용해 숫자로 변환 후 -97
y = int(n[1])-1 # -1 해서 시작위치 좌표화
arr = [[0]*8 for _ in range(8)] # 체스판

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8: # 범위 안에 있다면
        cnt += 1
print(cnt)