def solve(lst):
    global ans
    v = [0] * N       # 경사로 지은 곳 체크
    i = 0
    j = i + 1

    while i < N - 1:
        # 경사로 불가능 1) 차이가 1 이상
        if abs(lst[i] - lst[j]) > 1:
            return 0

        # 왼쪽이 작은 경우
        if lst[i] < lst[j]:             # i 포함 왼쪽으로 L만큼 i와 같아야함
            for l in range(L):          # 경사로 불가능 2) L만큼 경사로 불가
                if not 0 <= i-l < N:    return 0  # 범위 체크
                if lst[i-l] != lst[i]:  return 0  # 같은지 체크
                if v[i-l]:              return 0  # 이미 경사로 지은 경우
                v[i-l] = 1              # 경사로 설치
            # 바로 다음 칸으로 이동
            i = j
            j = i + 1

        # 오른쪽이 작은 경우
        elif lst[i] > lst[j]:           # j 포함 오른쪽으로 L만큼 j와 같아야함
            for l in range(L):
                if not 0 <= j+l < N:    return 0
                if lst[j] != lst[j+l]:  return 0
                if v[j+l]:              return 0
                v[j+l] = 1
             # 경사로 크기만큼 이동
            i = i + L
            j = i + 1

        # 같은 숫자인 경우 한 칸 이동
        else:
            i = j
            j = i + 1

    return 1

N,L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for r in range(N):
    if solve(arr[r]):
        ans += 1
arr = list(map(list,zip(*arr)))
for r in range(N):
    if solve(arr[r]):
        ans += 1

print(ans)