money = 1000 - int(input())
count = 0
for i in [500, 100, 50, 10, 5, 1] :
    count = count + money//i
    money = money%i
print(count)