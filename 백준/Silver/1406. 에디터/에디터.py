import sys

left = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
right=[]

for _ in range(m) :
  com = list(map(str,sys.stdin.readline().rstrip().split()))
  if com[0] == "L" and left:
    right.append(left.pop())
  elif com[0] =="D" and right:
    left.append(right.pop())
  elif com[0] =="B" and left :
    left.pop()
  elif com[0] =="P" :
    left.append(com[1])

print("".join(left)+"".join(reversed(right)))