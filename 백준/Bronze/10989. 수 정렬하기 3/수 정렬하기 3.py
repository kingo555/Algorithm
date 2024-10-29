import sys

n = int(sys.stdin.readline().rstrip())
lst=[0]*(10001)

for _ in range(n) :
    lst[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(lst)) :
    if lst[i]!=0 :
        for _ in range(lst[i]) :
            print(i)