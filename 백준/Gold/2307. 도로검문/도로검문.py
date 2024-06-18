import sys, heapq
input = sys.stdin.readline

def dij(s, remove):
    dist = [21e8] * (N + 1)
    dist[1] = 0
    q = [(0, s)]
    while q:
        cd, cur = heapq.heappop(q)
        if cur == remove: continue # 막은 도로
        if dist[cur] < cd: continue # 이미 더 작은 경우 패스
        for nxt, nd in adj[cur]:
            d = cd + nd
            if d < dist[nxt]:
                dist[nxt] = d
                heapq.heappush(q, (d, nxt))
    return dist[N]

N,M = map(int, input().split())
adj = [list() for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int, input().split())
    adj[a].append((b,t))
    adj[b].append((a,t))

# 기존 탈출 시간
origin = dij(1, 0)
new = 0

# 도로 하나씩 막기
for i in range(2, N+1):
    new = max(new, dij(1, i))

print(new - origin if new < 21e8 else -1)