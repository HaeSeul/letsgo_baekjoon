import sys
sys.setrecursionlimit(10**5)

def bfs(A):
    q = [(A, 0)]
    while q:
        c, d = q.pop(0)
        if c == B:
            return d+1
        if c < B:
            q.append((c*2, d+1))
            q.append((c*10+1, d+1))
    return -1

A,B=map(int, input().split())
print(bfs(A))