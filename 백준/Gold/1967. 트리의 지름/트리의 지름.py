from collections import deque, defaultdict

def bfs(s):
    global ans
    v = [-1] * (N+1)
    v[s] = 0
    q = deque([s])
    mx_node, mx_dist = 0,0
    while q:
        c = q.popleft()
        for e, w in adj[c]:
            if v[e] != -1 : continue
            q.append(e)
            v[e] = v[c] + w
            if mx_dist < v[e]:
                mx_node, mx_dist = e, v[e]
    ans = mx_dist
    return mx_node

ans = 0
N = int(input())
adj = defaultdict(list)
for _ in range(N-1):
    p, c, w = map(int, input().split())
    adj[p].append((c,w))
    adj[c].append((p,w))

n = bfs(bfs(1))
print(ans)