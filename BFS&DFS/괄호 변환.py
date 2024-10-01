def isRight(p):

    stk = []

    if len(p) == 0:
        return False

    for c in p:
        if c == '(':
            stk.append(c)
        else:
            if c == ')':
                if len(stk) == 0:
                    return False
                stk.pop()

    if len(stk) == 0:
        return True
    else:
        return False

def addU(u):

    u = u[1:len(u)-1]

    newU = ""

    for c in u:
        if c == '(':
            newU += ')'
        else:
            newU += '('

    return newU

def dfs(p):

    if len(p) == 0:
        return ""

    res = isRight(p)
    if res == True:
        return p

    open = 0
    close = 0
    pos = 0

    u = ""

    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1

        u += p[i]

        if open == close:
            pos = i
            break

    v = p[pos+1:len(p)]

    result = isRight(u)

    if result == True:
        return u + dfs(v)
    else:
        tmp = ""
        tmp += "("
        tmp += dfs(v)
        tmp += ")"
        tmp += addU(u)

        return tmp

def solution(p):
    answer = dfs(p)
    return answer

