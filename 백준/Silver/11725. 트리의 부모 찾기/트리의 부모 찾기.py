from collections import deque, defaultdict

N = int(input())
adj = defaultdict(list)
for i in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = [0]*(N+1)
q = deque()
for i in adj[1]:
    q.append(i)
    ans[i] = 1

while q:
    c = q.popleft()
    for i in adj[c]:
        if i==1: continue
        if ans[i]: continue
        ans[i] = c
        q.append(i)

print(*ans[2:], sep='\n')