import sys

n = int(sys.stdin.readline().rstrip())
name=[]

for _ in range(n) :
    [a, b] = map(str, sys.stdin.readline().rstrip().split())
    name.append([int(a),b])
name.sort(key=lambda x : x[0])

for i in range(n) :
    print(name[i][0], name[i][1])