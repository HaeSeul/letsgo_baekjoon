import sys
input = sys.stdin.readline

def make_tbl(ptn):
    tbl = [0] * len(ptn)
    i = 0   # 접두사 인덱스

    # 접두사 인덱스 이후부터 접미사 인덱스 시작
    for j in range(1, len(ptn)):

        # 패턴 내 접두==접미 구간이 아니라면
        while i>0 and ptn[i]!=ptn[j]:
            # 이전까지 같았던 구간으로 이동
            i = tbl[i-1]

        # 접두==접미라면
        if ptn[i]==ptn[j]:
            i += 1      # 접두 인덱스 증가
            tbl[j] = i  # 해당 접두의 개수까지는 일치한다고 갱신
    return max(tbl)

txt = input().rstrip()
ans = 0

# 텍스트를 하나씩 줄여가며 접두사로 만들어주기
for i in range(len(txt)):
    ans = max(ans, make_tbl(txt[i:]))
print(ans)