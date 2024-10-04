n = int(input())
p = list(map(int, input().split()))
time = 0
for i in range(0,n-1) :
    for j in range(0,n-1) :
        if p[j]>=p[j+1] :
            continue
        else :
            temp = p[j]
            p[j] = p[j+1]
            p[j+1] = temp    
            
for k in range(1,n+1) :
    time += k*p[k-1]
print(time)