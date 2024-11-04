import sys
sys.setrecursionlimit(10**9)

def dfs(node, cnt) :
    visited[node] = 1

    for adj_node in air[node] :
        if visited[adj_node] == 0 :
            cnt = dfs(adj_node, cnt+1)

    return cnt

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n, m = map(int, sys.stdin.readline().rstrip().split())
    air=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    
    for i in range(m) :
        a, b = map(int, sys.stdin.readline().rstrip().split())
        air[a].append(b)
        air[b].append(a)

    print(dfs(1,0))
