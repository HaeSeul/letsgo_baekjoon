import sys
input = sys.stdin.readline

s = []  # 현재까지 (인덱스, 높이)
mx = 0

N = int(input())
for i in range(N):
    now = int(input())
    idx = i

    while s and s[-1][1] >= now:    # 더이상 직사각형 확장 불가할 때까지
        idx, h = s.pop()
        mx = max(mx, (i-idx) * h)
    s.append((idx, now))          # 현재 인덱스와 높이 추가

# 남아있는 막대 탐색
while s:
    idx, h = s.pop()
    mx = max(mx, (N-idx) * h)

print(mx)