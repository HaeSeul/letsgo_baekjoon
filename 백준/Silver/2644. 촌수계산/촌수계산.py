def bfs(s):
    visited = [0]*(n+1)
    q = [(s,0)]     # 시작점, 번호
    visited[s] = 1

    while q:
        now, d = q.pop()
        if now==e:
            return d
        for next in adj[now]:
            if not visited[next]:
                q.append((next, d+1))
                visited[next]=1
    return -1


n = int(input())
s,e = map(int, input().split())
m = int(input())    # 관계 개수
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(s))