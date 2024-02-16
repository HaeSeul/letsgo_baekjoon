# N개 물건, 최대 무게 K
N,K = map(int, input().split())
# (무게, 가치) => dp table과 인덱스 맞춰주기 위해 [0] 추가
a = [0]+[list(map(int, input().split())) for _ in range(N)]
# 무게(i)에 맞게 각 물건(j)을 넣을 때마다 최대 value 갱신
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(1,K+1):
    for j in range(1,N+1):
        # 각 물건(j)
        w,v = a[j]
        # 내 무게(w)보다 현재 무게(i)가 크거나 같은 경우에만 가능
        if w <= i:
            # 나를 뽑기 전 상태에서 나를 추가했을 때 vs 나를 뽑지 않고 그냥 갈 때
            dp[i][j] = max(dp[i-w][j-1] + v, dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]
print(dp[K][N])