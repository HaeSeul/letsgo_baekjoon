import sys
input = sys.stdin.readline

def dfs(n,s,sm):
    global ans
    if L <= sm <= R and max(tmp)-min(tmp) >= X:
        ans += 1
    if sm > R:        # sum이 R보다 큰 경우
        return
    if n==N:
        if sm < L:    # 끝까지 갔는데 L보다 작은 경우
            return
        elif max(tmp)-min(tmp) < X:
            return
        return
    for i in range(s, N):
        tmp.append(A[i])
        dfs(n+1, i+1, sm+A[i])
        tmp.pop()

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
tmp = []
# 0개 뽑은 상태, start, sum=0
dfs(0,0,0)
print(ans)