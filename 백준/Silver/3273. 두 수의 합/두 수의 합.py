import sys

n = int(sys.stdin.readline().rstrip())
lst = set(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

count = 0

for i in lst :
    if x-i in lst :
         count += 1

print(int(count/2))