import sys
input = sys.stdin.readline

'''
L <= 2 문제 이상의 합 <= R
X <= max(level)-min(level)

중복 없이 조합
가능한 문제 가지수 : N개 중 2개 ~ N개 뽑기
문제를 하나씩 더해가며 R보다 커지면 back
전체 다 선택했는데 L보다 작다면 0
'''

def dfs(n,cnt,sm,mx,mn):
    global ans

    if n==N:
        if cnt>=2 and L <= sm <= R and mx-mn >= X:
            ans += 1
        return

    if sm > R:  return      # sum이 R보다 큰 경우

    # n번째 포함하지 않는 경우
    dfs(n+1, cnt, sm, mx, mn)
    # n번재 포함하는 경우
    dfs(n+1, cnt+1, sm+A[n], max(mx, A[n]), min(mn, A[n]))


N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
tmp = []
# 0개 뽑은 상태, cnt, sum, max, min
dfs(0,0,0,0,10**7)
print(ans)