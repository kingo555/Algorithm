T = int(input())

for _ in range(T) :
    money = int(input())
    for j in [25,10,5,1] :
        print(money//j,end=' ')
        money = money%j