import sys

n = int(sys.stdin.readline().rstrip())
cards = set(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))

for i in m_list :
    if i in cards :
        print(1,end=' ')
    else :
        print(0,end=' ')       