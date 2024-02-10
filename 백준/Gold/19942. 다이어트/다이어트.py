def dfs(n, start, p, f, s, v, c):
    global min_cost

    # 최소 비용을 넘어간다면 가지치기
    if c > min_cost:    return

    # N개를 다 골랐다면 끝
    if n > N:   return

    # 최저 영양소 기준 이상인지 확인
    if p >= mp and f >= mf and s >= ms and v >= mv:
        min_cost = c
        ans.append((c, *tmp))
        return

    for i in range(start, N):
        tmp.append(i+1)
        dfs(n+1, i+1, p+arr[i][0], f+arr[i][1], s+arr[i][2], v+arr[i][3], c+arr[i][4])
        tmp.pop()

# 식재료 개수
N = int(input())
# 단백질, 지방, 탄수화물, 비타민 (+가격)
mp,mf,ms,mv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp = []
ans = []
min_cost = 9876543210

dfs(0,0,0,0,0,0,0)

if not ans:
    print(-1)
else:
    ans.sort(key = lambda x : (x[0], x[1]))
    print(ans[0][0])
    print(*ans[0][1:])