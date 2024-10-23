import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    list = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    r = 0
    flag = 0
    
    if n == 0 :
      list=deque()
      
    for i in p :
      if i=="R" :
        r += 1
      elif i =="D" :
        if len(list) == 0 :
          print("error")
          flag = 1
          break
        else :
          if r %2 == 1 :
            list.pop()
          else :
            list.popleft()
    if r % 2==1 :
      list.reverse()

    if flag ==0 :
      print("["+",".join(list)+"]")