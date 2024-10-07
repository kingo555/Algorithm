import sys
import heapq

n = int(sys.stdin.readline())
timeline = []
for _ in range(n):
  start, end = map(int, sys.stdin.readline().split())
  timeline.append((start, end))
timeline.sort()

room = []
heapq.heappush(room, timeline[0][1])

for i in range(1,n) :
  if timeline[i][0] < room[0] :
    heapq.heappush(room, timeline[i][1])
  else :
    heapq.heappop(room)
    heapq.heappush(room, timeline[i][1])
print(len(room))