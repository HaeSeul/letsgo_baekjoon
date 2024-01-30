V = int(input())
E = int(input())
v = [0]*(V+1)

adj = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

ans = 0
s = [1]
while s:
    c = s.pop()
    if not v[c]:
        v[c]=1
        if c!=1:    # 시작점 제외
            ans+=1
        for n in adj[c]:
            if not v[n]:
                s.append(n)
print(ans)