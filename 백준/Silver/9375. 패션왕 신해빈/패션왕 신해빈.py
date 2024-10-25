import sys

input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t) :
    n = int(input().rstrip())
    clothes={}
    count=1

    for _ in range(n) :
        wear = input().rstrip().split()
        if wear[1] in clothes :
            clothes[wear[1]].append(wear[0])
        else :
            clothes[wear[1]]=[wear[0]]

    for i in clothes :
        count *= (len(clothes[i])+1)
    print(count-1)