def dfs(n):
    if n==M:
        print(*a)
        return
    for i in range(1, N+1):
        if not v[i]:
            v[i]=1
            a.append(i)
            dfs(n+1)
            a.pop()
            v[i]=0

# 1부터 N까지 중복없이 길이가 M인 수열
N,M = map(int, input().split())
v = [0]*(N+1)
a = []
dfs(0)
