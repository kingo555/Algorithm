import sys

n = int(sys.stdin.readline().rstrip())
lst=[]

for _ in range(n) :
    [a, b] = map(int,sys.stdin.readline().rstrip().split())
    lst.append([a,b])

lst.sort()
for i in range(n) :
    print(lst[i][0], lst[i][1])