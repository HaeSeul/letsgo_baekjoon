def cal(team):
    sm = 0
    # 팀 별 능력치 합 구하기
    for i in team:
        for j in team:
            if i!=j:    sm += arr[i][j]
    return sm


def split(n,s):
    global mn
    if n == N//2:
        # 팀 분배
        link = []
        for x in range(N):
            if x not in start:
                link.append(x)
        # 각 팀의 점수 합의 최소
        mn = min(mn, abs(cal(start) - cal(link)))
        return
    for i in range(s, N):
        start.append(i)
        split(n+1, i+1)
        start.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = N*N*100
# N명을 2개 팀으로 나누기 : N개 중 N/2개 뽑기
start = []
split(0,0)
print(mn)