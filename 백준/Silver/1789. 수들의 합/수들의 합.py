import sys

s = int(sys.stdin.readline())
n = 0
nature = 0
while s>0 :
  nature += 1
  s -= nature
  if s<0 :
    break
  n += 1
print(n)