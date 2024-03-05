def start_sm(n, s):
    global a_sm, tmp1
    if n == 2:  # 각 팀에서 둘 씩 계산
        x,y = tmp1[0], tmp1[1]
        a_sm += arr[x][y] + arr[y][x]
        return
    for i in range(s, N//2):
        tmp1.append(start[i])
        start_sm(n+1, i+1)
        tmp1.pop()

def link_sm(n, s):
    global b_sm, tmp2, link
    if n == 2:  # 각 팀에서 둘 씩 계산
        x,y = tmp2[0], tmp2[1]
        b_sm += arr[x][y] + arr[y][x]
        return
    for i in range(s, N//2):
        tmp2.append(link[i])
        link_sm(n+1, i+1)
        tmp2.pop()

def cal(start):
    global a_sm, b_sm, tmp1, tmp2, link
    a_sm, b_sm = 0,0

    link = []
    # start, link 팀 분배
    for x in range(N):
        if x not in start:
            link.append(x)
    tmp1, tmp2 = [], []
    start_sm(0,0)
    link_sm(0,0)
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