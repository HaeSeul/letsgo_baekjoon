import sys
input = sys.stdin.readline

def table(ptn):
    tb = [0] * len(ptn)
    i = 0   # 접두

    # 1부터 접미 돌리기
    for j in range(1, len(ptn)):
        # 패턴 내 접두==접미 구간이 아니라면
        while i>0 and ptn[i]!=ptn[j]:
            # 이전까지 같았던 구간으로 이동
            i = tb[i-1]
        # 접두==접미라면
        if ptn[i]==ptn[j]:
            i += 1      # 접두 인덱스 증가
            tb[j] = i   # 해당 접두의 개수까지 일치한다고 갱신
    return tb

def KMP(T, P):
    tb = table(P)   # 패턴 전처리 테이블
    cnt = 0         # 패턴이 나오는 횟수
    i = 0

    # 0부터 텍스트와 패턴 비교
    for j in range(len(T)):
        # 텍스트와 패턴이 다른 구간이라면
        while i>0 and P[i]!=T[j]:
            # 패턴 내 지금까지 같았던 구간 이후 인덱스로 이동
            i = tb[i-1]
        if P[i]==T[j]:
            i += 1           # 패턴 인덱스 증가
            if i == len(P):  # 패턴의 끝까지 갔다면
                cnt += 1
                i = tb[i - 1]  # 지금까지 같았던 구간 이후로 이동
    return cnt

N = int(input())
P = input().split()
T = input().split()

# 텍스트를 2배로 늘려서 순환 (마지막 인덱스까지 같아지면 0번째와 중복발생)
T += T[:-1]
cnt = KMP(T,P)

# 최대공약수 찾기
for i in range(cnt, 0, -1):
    if cnt%i==0 and N%i==0:
        print(f'{cnt//i}/{N//i}')
        break