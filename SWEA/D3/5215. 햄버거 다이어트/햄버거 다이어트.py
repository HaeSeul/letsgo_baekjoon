def dfs(n, sm, value):
    global ans
    if sm > L:  return  # sum이 Limit 넘으면 가지치기
    if n==N:
        if sm <= L:
            ans = max(ans, value)
        return

    # 현재 재료 포함
    dfs(n + 1, sm + a[n][1], value + a[n][0])
    # 현재 재료 미포함
    dfs(n + 1, sm , value)

T = int(input())
for tc in range(1, T+1):
    N,L = map(int, input().split())
    # [0]: 맛점수, [1]: 칼로리
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 0개 뽑은 상태, 칼로리총합, 맛총합
    dfs(0,0,0)
    print(f'#{tc} {ans}')