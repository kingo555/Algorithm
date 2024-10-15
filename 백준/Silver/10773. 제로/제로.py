import sys

k = int(sys.stdin.readline())
list = []
for _ in range(k) :
  a = int(sys.stdin.readline())
  if a==0 :
    list.pop()      
  else :
    list.append(a)

print(sum(list))