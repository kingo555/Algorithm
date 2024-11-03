import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n+1)]

for _ in range(n-1) :
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(node) :
    for i in graph[node] :
        if visited[i] == 0 :
            visited[i] = node
            dfs(i)

dfs(1)

for x in range(2, n+1) :
    print(visited[x])