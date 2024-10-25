import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
list = list(map(int, sys.stdin.readline().rstrip().split()))
q = deque(i for i in range(1,n+1))
count = 0

for x in list :
    while True :
        if q[0] == x :
            q.popleft()
            break
        elif q.index(x) > len(q)/2 :
            while q[0] != x :
                count+= 1
                q.appendleft(q.pop())
        else :
            while q[0] != x :
                count+= 1
                q.append(q.popleft())

print(count)
