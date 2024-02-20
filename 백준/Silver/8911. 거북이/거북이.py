import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c = input().rstrip()
    dir = ((-1,0),(0,1),(1,0),(0,-1))
    d = 0
    ci,cj = mx_i,mx_j = mn_i,mn_j = 0,0
    for s in c:
        if s=='L':
            d = (d-1)%4
        elif s=='R':
            d = (d+1)%4
        elif s=='F':
            ci,cj = ci+dir[d][0], cj+dir[d][1]
        else:
            ci,cj = ci-dir[d][0], cj-dir[d][1]

        # i,j의 이동거리 갱신
        mx_i, mx_j = max(mx_i, ci), max(mx_j, cj)
        mn_i, mn_j = min(mn_i, ci), min(mn_j, cj)
    print(abs(mx_i-mn_i) * abs(mx_j-mn_j))