import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

cards.sort()
answer = {}

for i in cards :
    if i in answer :
        answer[i] += 1
    else :
        answer[i] = 1

for i in m_list :
    if i in answer :
        print(answer[i],end=' ')
    else :
        print('0',end=' ')