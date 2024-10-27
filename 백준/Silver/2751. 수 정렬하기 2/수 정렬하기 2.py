import sys

n = int(sys.stdin.readline().rstrip())
list = []

for _ in range(n) :
    list.append(int(sys.stdin.readline().rstrip()))
list.sort()

for i in list :
    print(i)