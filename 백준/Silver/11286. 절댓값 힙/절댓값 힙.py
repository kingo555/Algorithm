import sys
import heapq

n = int(sys.stdin.readline().rstrip())
q = []
for _ in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
        if len(q)==0 :
            print(0)
        else :
            print(heapq.heappop(q)[1])
    else :
        heapq.heappush(q,(abs(x),x))