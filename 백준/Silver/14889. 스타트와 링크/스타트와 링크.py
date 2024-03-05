def cal(start):
    a_sm, b_sm = 0,0

    # 팀 분배
    link = []
    for x in range(N):
        if x not in start:
            link.append(x)
    
    # 팀 별 능력치 합 구하기
    for i in start:
        for j in start:
            if i!=j:    a_sm += arr[i][j]
    for i in link:
        for j in link:
            if i!=j:    b_sm += arr[i][j]

    return abs(a_sm - b_sm)


def split(n,s):
    global mn
    if n == N//2:
        mn = min(mn, cal(start))
        return
    for i in range(s, N):
        start.append(i)
        split(n+1, i+1)
        start.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = 21e8
# N명을 2개 팀으로 나누기 : N개 중 N/2개 뽑기
start = []
split(0,0)
print(mn)