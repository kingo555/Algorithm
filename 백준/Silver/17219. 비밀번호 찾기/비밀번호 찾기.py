import sys

n, m= map(int,sys.stdin.readline().rstrip().split())
site={}

for _ in range(n) :
    a,b = map(str, sys.stdin.readline().rstrip().split())
    site[a] = b

for _ in range(m) :
    a = sys.stdin.readline().rstrip()
    print(site[a])