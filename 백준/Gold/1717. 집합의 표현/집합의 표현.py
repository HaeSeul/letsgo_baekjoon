def find(a):
    if p[a]!=a:
        p[a] = find(p[a])
    return p[a]

def union(a,b):
    p[find(b)] = find(a)

N,M=map(int, input().split())
p=[i for i in range(N+1)]

for _ in range(M):
    cal, a, b = map(int, input().split())
    if cal==0:
        union(a,b)
    else:
        print('YES' if find(a)==find(b) else 'NO')