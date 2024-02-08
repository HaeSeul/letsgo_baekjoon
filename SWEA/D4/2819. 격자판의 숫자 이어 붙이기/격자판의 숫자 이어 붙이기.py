from collections import deque

def dfs(n,ci,cj):
    global ans
    # 총 길이가 7개가 됐다면 추가
    if len(n)==7:
        tmp.add(n)
        return

    # 4방 탐색하며 가능한 경우 모두 dfs
    for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<4 and 0<=nj<4:
            # 현재에 다음 문자 붙여서 dfs
            dfs(n+arr[ni][nj],ni,nj)

T = int(input())
for tc in range(1, T+1):
    # 문자열로 받기
    arr=[list(input().split()) for _ in range(4)]

    # 중복 제거를 위해 set 사용
    tmp=set()
    for i in range(4):
        for j in range(4):
            dfs('', i, j)

    print(f'#{tc} {len(tmp)}')