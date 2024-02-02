from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def bfs(s):
    v = [0]*100001
    v[s] = 1
    q = deque([(s,0)])
    ans = 0
    mn = 100001
    while q:
        c,d = q.popleft()
        if mn < d:          # 최소이동횟수보다 커진다면 끝
            return mn, ans
        if c == K:          # n중에서 K와 같다면 최소이동횟수 mn에 저장
            mn = min(mn, d)
            if mn == d:     # 현재가 최소이동횟수라면 ++
                ans += 1
        v[c] = 1    # 해당 이동 횟수에서 정답이 또 있을 수 있기 때문에 나중에 방문
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