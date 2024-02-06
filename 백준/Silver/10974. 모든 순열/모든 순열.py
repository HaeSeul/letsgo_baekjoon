N = int(input())
# 순열(중복X)
def dfs(n):
    if n==N+1:
        print(*a)
        return
    for i in range(1, N+1):
        if not v[i]:
            v[i]=1
            a.append(i)
            dfs(n+1)
            v[i]=0
            a.pop()

a = []
v = [0]*(N+1)   # 뽑지 않은 것들 중 선택
dfs(1)  # 1부터 시작