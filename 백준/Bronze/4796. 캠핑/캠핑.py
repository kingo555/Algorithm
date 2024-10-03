# 캠핑
count=1
while (True) :
    L, P, V = map(int, input().split())
    if (L==P==V==0) :
        break
    a = V//P
    b = V%P
    if L<b :
        b=L
    print("Case %d: %d" %(count,a*L+b))
    count+=1