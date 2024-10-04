n = int(input())
p =list(map(int, input().split()))
time = 0
p.sort()
for i in range(1, n+1) :
    time = time + sum(p[0:i])
print(time)