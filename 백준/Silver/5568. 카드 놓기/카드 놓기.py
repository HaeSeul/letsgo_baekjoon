def dfs(n):
    global ans
    if n==K:    # K개 뽑으면 종료
        if ''.join(tmp) not in ans:
            ans.append(''.join(tmp))
        return

    for i in range(N):
        if not v[i]:
            v[i]=1
            tmp.append(lst[i])
            dfs(n+1)
            v[i]=0
            tmp.pop()

# N장 중 K장 선택해서 만들 수 있는 가지수 (순열)
N = int(input())
K = int(input())
lst = list(input() for _ in range(N))
v = [0]*N   # lst 요소 선택했는지 확인
tmp = []
ans = []    # 이전 조합에 있는지 확인
# 0개 뽑은 상태
dfs(0)
print(len(ans))