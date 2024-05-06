import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

'''
트리
    - 정점 n, 간선 n-1
    - 사이클 X
    - 임의의 두 정점에 대해 경로가 유일
'''
from collections import defaultdict, deque

def bfs(i):
    tree = True
    q = deque([i])
    while q:
        c = q.popleft()
        if v[c]: tree = False   # 사이클

        v[c] = True
        for j in adj[c]:
            if v[j]: continue
            q.append(j)
    return tree

tc = 1
while True:
    N,M = map(int, input().split())
    if (N,M) == (0,0): break

    adj = defaultdict(list)
    v = [0] * (N+1)
    cnt = 0

    for _ in range(M):
        x,y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    for i in range(1, N+1): # 1부터 시작
        if v[i]: continue
        if bfs(i): cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')

    tc += 1