import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
dic={}

for i in range(1,n+1) :
    a = sys.stdin.readline().rstrip()
    dic[i] = a
    dic[a] = i
    
for _ in range(m) :
    b = sys.stdin.readline().rstrip()
    if b.isdigit() :
        print(dic[int(b)])
    else :
        print(dic[b])