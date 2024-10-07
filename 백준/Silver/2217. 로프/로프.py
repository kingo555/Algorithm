import sys

n = int(sys.stdin.readline())
rope = []
weight = 0 
for _ in range(n) :
  rope.append(int(sys.stdin.readline()))
rope.sort()

for i in range(len(rope)) :
  if weight<= rope[i]*(len(rope)-i) :
    weight = rope[i]*(len(rope)-i)
print(weight)