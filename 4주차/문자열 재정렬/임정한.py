X = [*input()]
X.sort()
num = 0
cnt = len(X)
for i in range(len(X)):
    if X[i]<"A":
        num+=int(X[i])
    else:
        cnt = i
        break
answer = ""
if num == 0:
    num = ""
print(answer.join(X[cnt:])+str(num))


#TESTCASE
#1. 3
#2. ABCD