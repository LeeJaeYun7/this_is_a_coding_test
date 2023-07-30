N = int(input())
cards = []
for i in range(N):
    cards.append(int(input()))
cards.sort()
sum = 0

for i in range(N):
    sum+=cards[i]*(N-i)
print(sum-cards[0])
10+20
