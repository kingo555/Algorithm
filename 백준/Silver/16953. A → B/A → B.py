a,b = map(int, input().split())
count = 1
while (b!=a) :
  temp = b
  count+=1
  if b%10==1 :
    b= b//10
  elif b%2==0 :
    b/= 2

  if temp==b :
    count=-1
    break
print(count)