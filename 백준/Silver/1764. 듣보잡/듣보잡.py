import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
count = 0
lis=set()
wat=set()
lw = []
for _ in range(n) :
    lis.add(sys.stdin.readline().rstrip())
for _ in range(m) :
    wat.add(sys.stdin.readline().rstrip())

for i in lis :
    if i in wat :
        count+=1
        lw.append(i)
lw.sort()
print(count)
for a in lw :
    print(a)