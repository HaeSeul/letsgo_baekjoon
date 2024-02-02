from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def bfs(s):
    v = [0]*100001
    q = deque([(s,0)])
    v[s] = 1
    ans = 0
    mn = 100001
    while q:
        c,d = q.popleft()
        if c == K:      # n중에서 K와 같다면 최소이동횟수 mn에 저장
            mn = min(mn, d)
            if mn == d:   # depth+1이 최소이동횟수라면 ++
                ans += 1
            elif mn < d:
                return mn, ans
        v[c] = 1
        for n in (c-1, c+1, c*2):
            if 0 <= n <= 100000 and not v[n]:
                q.append((n,d+1))
    return mn, ans

# 수빈 N -> 동생 K
N,K = map(int, input().split())
sec, way = 0, 0
if N==K:
    way = 1
else:
    sec, way = bfs(N)
print(sec, way, sep='\n')