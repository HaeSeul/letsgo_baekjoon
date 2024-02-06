def dfs(n):
    global mx
    if n==N:        # N개 다 뽑은 후 식 계산
        sm = 0
        for i in range(1, N):  # N-1번 실행
            sm += abs(tmp[i-1]-tmp[i])
        mx = max(mx, sm)
        return
    for i in range(N):
        if not v[i]:
            v[i]=1
            tmp.append(A[i])
            dfs(n+1)
            v[i]=0
            tmp.pop()


N = int(input())
A = list(map(int, input().split()))
v = [0]*N
tmp = []    # 식 계산을 위해 뽑은 수 저장
mx = -1000

dfs(0)  # 0개 뽑은 상태
print(mx)