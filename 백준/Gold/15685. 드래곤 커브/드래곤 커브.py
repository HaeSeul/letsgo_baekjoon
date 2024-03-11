def rotate_left(curve):
    lst = []
    for ci, cj in curve:
        ni, nj = ci, cj * (-1)
        lst.append((nj, ni))
    return lst


def make_curve(curve, g):
    for n in range(g):
        ei, ej = curve[-1]
        nxt_ei, nxt_ej = ej, ei * (-1)
        di, dj = ei - nxt_ei, ej - nxt_ej

        nxt = []
        # 현재 도형 90도 회전
        for ci, cj in curve:
            ni, nj = cj, ci * (-1)
            nxt.append((ni, nj))
        # 이어붙이기 (e의 앞부터 붙이기)
        for curr in range(len(nxt) - 2, -1, -1):
            c = nxt[curr]
            ni, nj = c[0] + di, c[1] + dj
            curve.append((ni, nj))
    return curve


N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    # 0세대 만들어놓기
    si, sj, ei, ej = 0, 0, 0, 1
    curve = [(si, sj), (ei, ej)]
    x, y, d, g = map(int, input().split())  # x,y -> 좌표 상에서 j,i

    curve = make_curve(curve, g)    # g 세대만큼 드래곤 만들기
    for _ in range(d):              # 첫 방향만큼 회전해주기
        curve = rotate_left(curve)
    for ci, cj in curve:            # arr에 1 찍기
        arr[ci + y][cj + x] = 1

# 정사각형이 되는 곳 찾기
ans = 0
for i in range(100):
    for j in range(100):
        if (arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]):
            ans += 1
print(ans)