import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    p,c,w = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append([c,w])
    graph[c].append([p,w])

def dfs(x, dist) :
    for i in graph[x] :
        node, weight= i
        if distance[node] == -1 :
            distance[node] = dist+weight
            dfs(node, dist+weight) 

distance = [-1]*(n+1)
distance[1] = 0
dfs(1,0)

res = distance.index(max(distance))
distance = [-1] * (n+1)
distance[res] = 0
dfs(res , 0)

print(max(distance))