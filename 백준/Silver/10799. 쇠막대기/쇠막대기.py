import sys

list = list(map(str,sys.stdin.readline().rstrip()))
count = 0
stack = []

for i in list :
    if i == '(' :
        stack.append(i)
    else :
        if before == '(' :
            stack.pop()
            count += len(stack)
        else :
            stack.pop()
            count += 1
    before = i
print(count)