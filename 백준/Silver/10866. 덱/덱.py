import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n) :
    com = list(sys.stdin.readline().rstrip().split())
    if com[0] == "push_front" :
        q.appendleft(com[1])
    elif com[0] == "push_back" :
        q.append(com[1])
    elif com[0] == "pop_front" :
        if len(q) != 0 :
            print(q[0])
            q.popleft()
        else :
            print(-1)
    elif com[0] == "pop_back" :
        if len(q) != 0 :
            print(q[-1])
            q.pop()
        else :
            print(-1)
    elif com[0] == "size" :
        print(len(q))
    elif com[0] == "empty" :
        if len(q) != 0 :
            print(0)
        else : 
            print(1)
    elif com[0] == "front" :
        if len(q) != 0 :
            print(q[0])
        else :
            print(-1)
    elif com[0] == "back" :
        if len(q) != 0 :
            print(q[-1])
        else :
            print(-1)