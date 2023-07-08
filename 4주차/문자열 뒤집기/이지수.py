import sys
sys.stdin = open("input1.txt")

S = input()
cnt = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1
print((cnt+1)//2)

# s = input()
# x = 0
# temp = 0
# temps = []
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         temp +=1
#     else:
#         temp += 1
#         temps.append(temp)
#         temp = 0
#
# print((len(temps)+1)//2)