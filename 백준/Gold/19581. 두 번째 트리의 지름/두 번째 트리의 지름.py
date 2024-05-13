import sys
input = sys.stdin.readline

from collections import defaultdict, deque

def bfs(s, flag):
    v = [-1 for _ in range(N+1)]
    v[s] = 0
    if flag: v[flag] = 0

    q = deque([s])
    mx_node, mx_dist = 0, 0
    while q:
        c = q.popleft()
        for e,w in adj[c]:
            if v[e] != -1: continue
            q.append(e)
            v[e] = v[c] + w
            if mx_dist <= v[e]:
                mx_node, mx_dist = e, v[e]
    if not flag: return mx_node
    else: return mx_dist

N = int(input())
adj = defaultdict(list)

for _ in range(N-1):
    a,b,w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))

a_node = bfs(1,0)
b_node = bfs(a_node,0)

print(max(bfs(a_node, b_node), bfs(b_node, a_node)))