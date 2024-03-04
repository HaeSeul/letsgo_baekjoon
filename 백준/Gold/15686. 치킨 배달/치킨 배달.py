def cal(choose):
    dist = 0     # 도시의 치킨거리
    for hi,hj in house:
        tmp = 21e8      # 각 집의 치킨거리
        for ci,cj in choose:
            tmp = min(tmp, abs(hi-ci)+abs(hj-cj))
        dist += tmp
    return dist


def dfs(n, s):
    global mn
    if n==M:    # M개 뽑은 경우 종료
        mn = min(mn, cal(choose))
        return
    for x in range(s, len(chick)):
        choose.append(chick[x])
        dfs(n+1, x+1)
        choose.pop()

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mn = 21e8

# 치킨집과 집의 위치 저장
chick = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chick.append((i,j))

# 치킨집 중 중복 없이 M개 뽑기
choose = []
dfs(0,0)
print(mn)