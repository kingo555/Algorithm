import sys
n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().strip().split()))
count=0
for i in number :
  if i==1 :
    continue
  for j in range(2,int(i**0.5)+1) :
    if i%j==0 :
      break
  else :
    count+=1
print(count)