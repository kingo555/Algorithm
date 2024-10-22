import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n,m = map(int, sys.stdin.readline().rstrip().split())
    q = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    count = 0
    
    while q :
        best = max(q)
        first = q.popleft()
        m -= 1
        
        if best == first :
            count += 1
            if m < 0 :
                print(count)
                break
        else :
            q.append(first)
            if m < 0 :
                m = len(q)-1