import sys

lst = list(map(int, sys.stdin.readline().rstrip().split()))

lst.sort()
print(lst[1])