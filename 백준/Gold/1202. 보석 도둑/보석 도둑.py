import sys
import heapq
n,k = map(int,sys.stdin.readline().split())
jewel = []
bag = []
q=[]
result = 0

for _ in range(n) :
  m, v = list(map(int, sys.stdin.readline().strip().split()))
  jewel.append((m,v))

for _ in range(k) :
  b = int(sys.stdin.readline())
  bag.append(b)

jewel.sort(key=lambda x: x[0], reverse=True)
bag.sort(reverse=True)

while bag :
  b= bag.pop()
  while jewel :
    weight, value = jewel.pop()
    if b >= weight :
      heapq.heappush(q, -value)
    else :
      jewel.append((weight,value))
      break
  if q:
    result -= heapq.heappop(q)
print(result)