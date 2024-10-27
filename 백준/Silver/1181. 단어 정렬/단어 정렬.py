import sys

n = int(sys.stdin.readline().rstrip())
lst = []

for _ in range(n) :
    lst.append(sys.stdin.readline().rstrip())
    
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst :
    print(i)