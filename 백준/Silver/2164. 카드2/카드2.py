import sys
from collections import deque

n = int(sys.stdin.readline())
heap = deque()

for i in range(1, n+1) :
  heap.append(i)

while len(heap)>1 :
  heap.popleft()
  heap.append(heap.popleft())
  
print(heap[0])