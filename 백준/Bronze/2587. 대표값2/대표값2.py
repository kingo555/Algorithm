import sys

lst = []
for _ in range(5) :
    a = int(sys.stdin.readline().rstrip())
    lst.append(a)

print(int(sum(lst)/5))
lst.sort()
print(lst[2])