N, K = map(int, input().split())
coin = []
count = 0
for i in range(N) :
    a = int(input())
    coin.append(a)

for j in range(N-1,-1,-1) :
    cnt = K//coin[j]
    count= count+cnt
    K = K%coin[j]
    if K==0 :
        break
print(count)