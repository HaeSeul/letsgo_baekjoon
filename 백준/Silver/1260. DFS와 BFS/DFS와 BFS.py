import sys
sys.setrecursionlimit(10**5)

def dfs(s):
    v[s] = 1
    print(s, end=' ')
    for n in adj[s]:
        if not v[n]:
            dfs(n)

def bfs(s):
    v2 = [0]*(N+1)
    q = [s]
    v2[s] = 1
    while q:
        c = q.pop(0)
        print(c, end=' ')
        for n in adj[c]:
            if not v2[n]:
                v2[n]=1
                q.append(n)

# 정점개수, 간선개수, 시작정점
N,M,V = map(int, input().split())
adj = [[] for _ in range(N+1)]
v = [0] * (N + 1)

for _ in range(M):
    v1,v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(N+1):
    adj[i] = sorted(adj[i])

dfs(V)
print()
bfs(V)
