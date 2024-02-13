def find(a):
    if p[a]!=a:
        p[a] = find(p[a])
    return p[a]

def union(a,b):
    p[find(b)] = find(a)

V,E = map(int, input().split())
p = [i for i in range(V+1)]

edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x:x[2])   # weight 기준 정렬

w = 0
for e in edges:
    if find(e[0]) != find(e[1]):    # 같은 집합이 아니라면
        union(e[0],e[1])            # 하나의 집합으로 갱신
        w += e[2]
print(w)