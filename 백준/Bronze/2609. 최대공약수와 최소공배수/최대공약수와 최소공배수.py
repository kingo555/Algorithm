import sys
n,m = map(int, sys.stdin.readline().split())
temp=[]

for i in range(1,min(n,m)+1) :
  if n%i==0 and m%i==0 :
    temp.append(i)

print(max(temp))
print(max(temp)*(n//max(temp)*(m//max(temp))))
