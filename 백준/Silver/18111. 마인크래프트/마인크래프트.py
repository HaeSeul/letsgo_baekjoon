def find_mnmx(tmp):
    mn, g = 300, 0    # 최대 높이 256
    for i in range(N):
        for j in range(M):
            mn = min(mn, tmp[i][j])
            g += tmp[i][j]
    return mn, g


N,M,B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time, mn_time = 0, 21e8
ans = 0

mn, g = find_mnmx(arr)  # 가능한 최소 높이, 현재 블록 개수
mx = (g+B) // (N*M)     # 가능한 최대 높이

# 가능한 최대 높이부터 최소까지 탐색
for h in range(mx, mn-1, -1):
    cut, fill = 0,0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > h:       # 현재 땅이 더 높다면 자르기
                cut += arr[i][j] - h
            elif arr[i][j] < h:     # 현재 땅이 더 낮다면 채우기
                fill += h - arr[i][j]

    time = cut * 2 + fill           # 걸리는 시간 확인

    if mn_time > time:              # 최소 시간 갱신 (같은 값일 경우 최대가 답)
        mn_time = time
        ans = h

print(mn_time, ans)