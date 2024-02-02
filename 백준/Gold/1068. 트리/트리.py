def dfs(s):
    lst[s] = -2
    for i in range(N):
        if s==lst[i]:
            dfs(i)

N = int(input())
lst = list(map(int, input().split()))
t = int(input())

dfs(t)  # 내 아래 자식들 모두 삭제
# 리프인지 확인 (내 인덱스를 가지고 있는 것이 있다면 나는 리프가 아님)
ans = 0
for i in range(N):
    if lst[i]!=-2 and i not in lst:
        ans += 1
print(ans)