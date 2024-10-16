import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deque = deque()

for i in range(n) :
  a = sys.stdin.readline().rstrip().split()
  
  if a[0]=="push" :
    deque.append(a[1])
  
  elif a[0]=="pop" :
    if deque :
      print(deque.popleft())
    else :
      print(-1)
  
  elif a[0]=="size" :
    print(len(deque))
  
  elif a[0]=="empty" :
    if deque :
      print(0)
    else : print(1)
  
  elif a[0]=="front" :
    if deque :
      print(deque[0])
    else :
      print(-1)
  
  elif a[0]=="back" :
    if deque :
      print(deque[-1])
    else :
      print(-1)
    