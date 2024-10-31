import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())
    lst = []
    cnt = 1
    
    for _ in range(n) :
        a,b = list(map(int, sys.stdin.readline().rstrip().split()))
        lst.append((a,b))
    
    lst.sort(key=lambda x : x[0])
    
    check = lst[0][1]
    for i in range(1,n) :
        if lst[i][1] < check :
            check = lst[i][1]
            cnt += 1
    print(cnt)