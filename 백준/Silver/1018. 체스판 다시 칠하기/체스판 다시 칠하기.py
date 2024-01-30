N,M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

str_WB='WBWBWBWB'
str_BW='BWBWBWBW'

cnt = []
for n in range(N-8+1):
    for m in range(M-8+1):
        cnt_WB = cnt_BW = 0
        # WB와 BW로 시작할 때 고치는 개수 세기
        for i in range(n, n+8, 2):
            for j in range(m, m+8):
                if arr[i][j] != str_WB[j-m]:  cnt_WB+=1
                if arr[i][j] != str_BW[j-m]:  cnt_BW+=1
        for i in range(n+1, n+8, 2):
            for j in range(m, m+8):
                if arr[i][j] != str_BW[j-m]:  cnt_WB+=1
                if arr[i][j] != str_WB[j-m]:  cnt_BW+=1
        cnt.append(min(cnt_WB, cnt_BW))
print(min(cnt))