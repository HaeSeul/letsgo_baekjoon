import sys
input = sys.stdin.readline
from collections import deque

# N*N, M개 나무 심기, K년 이후
N,M,K = map(int, input().split())
arr = [[5]*N for _ in range(N)]
age = [[deque() for _ in range(N)] for _ in range(N)]
dir = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

# 매 겨울마다 추가되는 양분
plus = [list(map(int, input().split())) for _ in range(N)]

# 초기 나무 심기
for _ in range(M):
    ti,tj,ta = map(int, input().split())    # i-1,j-1 해주기
    age[ti-1][tj-1].append(ta)

# K년 반복
for _ in range(K):
    grow = [[0]*N for _ in range(N)]

    # 1. 양분먹거나 죽기
    for i in range(N):
        for j in range(N):
            if not age[i][j]: continue  # 나무가 없는 경우

            dead = 0
            trees = age[i][j]

            for n in range(len(trees)):
                tree = trees.popleft()
                if arr[i][j] >= tree:           # 양분이 충분하다면
                    arr[i][j] -= tree           # 나이만큼 양분 추가
                    age[i][j].append(tree+1)    # 1살 더 먹기
                    if (tree+1)%5 == 0:         # 5의 배수라면 가을에 번식
                        grow[i][j] += 1
                else:                           # 양분이 부족하다면 죽음
                    dead += (tree // 2)

            arr[i][j] += dead    # 죽은만큼 추가

    # 2. 나무번식 + 양분추가
    for i in range(N):
        for j in range(N):
            if grow[i][j]:
                cnt = grow[i][j]
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N): continue
                    for _ in range(cnt):    # 자라야하는 만큼 추가
                        age[ni][nj].appendleft(1)
            arr[i][j] += plus[i][j]

# 살아남은 나무 개수
ans = 0
for i in range(N):
    for j in range(N):
        if not age[i][j]: continue
        ans += len(age[i][j])
print(ans)