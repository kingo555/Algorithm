n = int(input())

stack = []
answer = []
cur=1
flag=0

for _ in range(1,n+1) :
    num = int(input())

    while cur <= num :
        answer.append("+")
        stack.append(cur)
        cur += 1

    if stack[-1] == num :
        stack.pop()
        answer.append("-")

    else :
        print("NO")
        flag = 1
        break
if flag == 0 :
    for i in answer:
        print(i)