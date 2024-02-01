import sys
sys.setrecursionlimit(10**5)

def bfs(A):
    q = [(A, 0)]
    v = []
    while q:
        c, d = q.pop(0)
        if c == B:
            return d+1
        x,y = c*2, int(str(c)+'1')
        if c not in v:
            v.append(c)
            if x<=B:
                q.append((x, d+1))
            if y<=B:
                q.append((y, d+1))
    return -1

A,B=map(int, input().split())
print(bfs(A))