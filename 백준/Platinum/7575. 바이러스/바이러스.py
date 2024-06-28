import sys
input = sys.stdin.readline

def make_tbl(ptn):
    tbl = [0] * len(ptn)
    i = 0   # 접두사 인덱스

    # 접두사 인덱스 이후부터 접미사 인덱스 시작
    for j in range(1, len(ptn)):

        while i>0 and ptn[i]!=ptn[j]:   # 패턴 내 접두==접미 구간이 아니라면
            i = tbl[i-1]                # 이전까지 같았던 구간으로 이동

        if ptn[i]==ptn[j]:  # 접두==접미라면
            i += 1          # 접두 인덱스 증가
            tbl[j] = i      # 해당 접두의 개수까지는 일치한다고 갱신

    return tbl


def KMP(virus):
    global ans

    res = [0] * N  # 바이러스가 있는 프로그램 확인

    # 순방향, 역방향 확인
    for v in (virus, virus[::-1]):
        tbl = make_tbl(v)  # 바이러스 전처리 테이블

        # 각 프로그램 확인
        for idx in range(1, N):
            # 이미 바이러스 있다고 판단했으면 패스
            if res[idx]: continue

            prgm = programs[idx]

            i = 0   # 바이러스 인덱스

            # 프로그램의 길이만큼 반복
            for j in range(len(prgm)):

                # 프로그램과 바이러스 비교
                while i>0 and v[i]!=prgm[j]:
                    i = tbl[i-1]

                if v[i]==prgm[j]:
                    i += 1
                    if i == K:          # 바이러스의 모든 부분과 일치한다면
                        res[idx] = 1    # 바이러스 발견!!
                        break           # 다음 프로그램 확인

    # 모든 프로그램에서 바이러스가 나왔다면 정답 갱신
    if res.count(1) == N-1:
        ans = 'YES'
        return


def solve():
    global ans

    # 프로그램을 K개의 연속 부분 수열로 나누기
    for s in range(len(programs[0]) - K + 1):

        # 정답 갱신했다면 종료
        if ans == 'YES': return

        virus = programs[0][s:s + K]
        cand = True
        for c in virus:
            # 모든 프로그램에 나오는 바이러스 번호만 확인
            if cnt[c] < N:
                cand = False
                break
        if not cand: continue
        KMP(virus)


N,K = map(int, input().split())
ans = 'NO'

cnt = [0] * 10001    # 프로그램마다 나오는 정수 개수 (최대 10000)
programs = []

for _ in range(N):
    _ = input()
    program = list(map(int, input().split()))
    programs.append(program)

    # 각 프로그램에 나온 정수 개수 카운팅
    for i in program:
        cnt[i] += 1

solve()
print(ans)