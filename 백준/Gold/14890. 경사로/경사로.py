def check_row(lst,v,i,j):
    # L 길이만큼 경사로를 지을 수 있는지 확인
    tmp = []

    if lst[i] < lst[j]:     # i 포함 왼쪽으로 L만큼 i와 같아야함
        for l in range(L):
            if not 0 <= i-l < N:    return []   # 범위 체크
            if lst[i-l] != lst[i]:  return []   # 같은지 체크
            if v[i-l]:              return []   # 이미 경사로 지은 경우
            tmp.append(i-l)   # 경사로 지을 곳 저장
        return tmp

    else:       # i가 큰 경우, j 포함 오른쪽으로 L만큼 j와 같아야함
        for l in range(L):
            if not 0 <= j+l < N:    return []
            if lst[j] != lst[j+l]:  return []
            if v[j+l]:              return []
            tmp.append(j+l)
        return tmp

def solve():
    global ans
    for r in range(N):
        v = [0 for _ in range(N)]       # 경사로 지은 곳 체크
        flag = 1  # 경사로 가능 여부
        i = 0
        j = i + 1
        lst = arr[r]

        while i < N - 1:
            # 경사로 불가능 1) 차이가 1 이상
            if abs(lst[i] - lst[j]) > 1:
                flag = 0
                break

            # 차이가 1인 경우, 경사로 놓을 수 있는지 확인
            elif abs(lst[i] - lst[j]) == 1:
                tmp = check_row(lst, v, i, j)
                # 경사로 불가능 2) L만큼 경사로 불가
                if not tmp:
                    flag = 0
                    break
                # 경사로 설치
                for x in tmp:
                    v[x] = 1

                if lst[i] < lst[j]:     # 바로 다음 칸으로 이동
                    i = j
                    j = i + 1
                else:       # 오른쪽이 작으면, 다음 파트로 경사로 크기만큼 이동
                    i = i + L
                    j = i + 1

            # 같은 숫자인 경우 한 칸 이동
            else:
                i = j
                j = i + 1

        if flag:
            ans += 1

N,L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

solve()
arr = list(map(list,zip(*arr[::])))
solve()
print(ans)