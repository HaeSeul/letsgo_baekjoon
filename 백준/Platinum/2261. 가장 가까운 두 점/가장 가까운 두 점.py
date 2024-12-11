def cal_dist(start, end):   # 범위 내 모든 점 거리 계산
    mn = float('inf')
    for i in range(start, end-1):
        for j in range(i+1, end):
            dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            mn = min(mn, dist)
    return mn

def find(start, end):   # 이분탐색으로 범위 좁히기
    size = end - start

    # 3개 미만으로 남으면 범위 내 모든 점들의 거리 계산
    if size < 3:
        return cal_dist(start, end)

    mid = (start + end) // 2
    # 왼/오 분할정복
    left = find(start, mid)
    right = find(mid, end)

    mn = min(left, right)

    # 왼/오 중간 점 탐색
    cand = []
    divider = points[mid][0]    # 중심이 될 x 축
    for i in range(start, end):
        # 중심축으로부터 mn 보다 작은 것들만 탐색 후보로
        if (points[i][0] - divider)**2 <= mn:
            cand.append(points[i])

    # y축 기준으로 정렬
    cand.sort(key=lambda x: x[1])

    for i in range(len(cand)):
        cur = cand[i]
        for j in range(i+1, len(cand)):
            nxt = cand[j]
            # y축 차이가 mn보다 크면 탐색 X
            if (nxt[1] - cur[1])**2 >= mn: break
            dist = (nxt[0] - cur[0])**2 + (nxt[1] - cur[1])**2
            mn = min(mn, dist)
    return mn

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x,y))

# x축 기준으로 정렬
points.sort()
print(find(0, N))