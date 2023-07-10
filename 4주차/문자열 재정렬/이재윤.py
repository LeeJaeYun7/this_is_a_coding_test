// 반드시 문자열을 정렬해줘야 한다
// 문자열을 정렬할 때, list로 변환해서 정렬하고, list를 다시 문자열로 만들어준다. 

name = input()
sum = 0 
ans = ''

for i in range(0, len(name)):
    if '0' <= name[i] and name[i] <= '9':
        sum += int(name[i])
    else:
        ans += name[i]
        
ansList = list(ans)
ansList.sort()
ans = ''.join(ansList)
        
ans += str(sum)

print(ans)
