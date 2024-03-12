from collections import defaultdict

def check(arr_copy):
    global ladder

    # 각 열마다 어디로 가는지 확인
    for j in range(M):
        ci,cj = 0,j

        # 바닥에 올 때까지 탐색
        while ci < N:
            if arr_copy[ci][cj] == 1:
                # 나에서 시작하는 사다리 : 오른쪽 아래 대각선으로 이동
                if ci in ladder[cj]:
                    ci,cj = ci+1, cj+1
                # 나한테 오는 사다리 : 왼쪽 아래 대각선으로 이동
                elif 0 <= cj-1 and ci in ladder[cj-1]:
                    ci,cj = ci+1, cj-1
            else:
                # 1을 만나기 전까지 아래로 이동
                ci += 1
        if j != cj: return 0
    return 1


def combination(n,s,target):
    global success, ladder
    if success: return
    # 1,2,3개 뽑는 경우 종료
    if n==target:
        arr_copy = [list(l) for l in arr[::]]

        # 사다리 만들기
        for x in choose:
            arr_copy[x[1]][x[0]], arr_copy[x[1]][x[0]+1] = 1,1

        if check(arr_copy):
            success = 1
        return

    for i in range(s,len(tmp)):     # (열, 행)
        c, r = tmp[i][0], tmp[i][1]
        choose.append((c, r))
        ladder[c].append(r)
        combination(n+1, i+1, target)
        ladder[c].pop()
        choose.pop()


# 열 N->M, 가로개수 M->H, 행 H->N
M,H,N = map(int, input().split())
arr = [[0]*M for _ in range(N)]

ladder = defaultdict(list)    # M번째 열에서 시작하는 N행의 사다리 정보
for _ in range(H):
    hi,hj = map(lambda x:x-1, map(int, input().split()))
    ladder[hj].append(hi)
    arr[hi][hj],arr[hi][hj+1] = 1,1     # 사다리놓기

# 놓을 수 있는 사다리
tmp = []
for m in range(M-1):
    for n in range(N):
        # 나와 내 앞/뒤 사다리에 없는 행만 추가
        if n in ladder[m]: continue
        if 0 <= m-1 and n in ladder[m-1]: continue
        if m+1 < N and n in ladder[m+1]: continue
        tmp.append((m,n))

ans = 0
success = 0
choose = []
if check(arr):   # 처음에 가능한지 확인
    print(ans)
else:
    for t in range(1, 4):
        combination(0,0,t)
        if success:
            ans = t
            break
    if not success:
        ans = -1
    print(ans)