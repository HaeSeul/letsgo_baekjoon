import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

from collections import defaultdict

def count(c):
    size[c] = 1
    for node in adj[c]:
        if not size[node]:
            count(node)
            size[c] += size[node]

# 정점N개, 루트R, 쿼리수Q
N,R,Q = map(int, input().split())
adj = defaultdict(list)

for _ in range(N-1):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

size = [0 for _ in range(N+1)]
count(R)

for _ in range(Q):
    print(size[int(input())])