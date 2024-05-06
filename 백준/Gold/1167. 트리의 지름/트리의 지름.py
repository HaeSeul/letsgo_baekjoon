from collections import deque

def bfs(s):
    global ans
    v = [-1] * (V+1)
    v[s] = 0
    q = deque([s])
    mx_node, mx_dist = 0,0
    while q:
        c = q.popleft()
        for e, w in adj[c]:
            if v[e] != -1: continue
            q.append(e)
            v[e] = v[c] + w
            if mx_dist < v[e]:
                mx_node, mx_dist = e, v[e]
    ans = mx_dist
    return mx_node

ans = 0
V = int(input())
adj = dict()

for _ in range(V):
    a = list(map(int, input().split()))
    adj[a[0]] = list()
    for x in range(1, len(a)-1, 2):
        adj[a[0]].append((a[x], a[x+1]))

n = bfs(bfs(1))
print(ans)