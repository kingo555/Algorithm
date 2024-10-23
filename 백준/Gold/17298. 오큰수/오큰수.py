import sys

n = int(sys.stdin.readline().rstrip())
list = list(map(int, sys.stdin.readline().rstrip().split()))
answer=[-1]*n
stack=[]

for i in range(n) :
  while stack and list[i] > list[stack[-1]] :
    answer[stack[-1]] = list[i]
    stack.pop()
  
  stack.append(i)

print(*answer)