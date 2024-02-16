# N개 물건, 최대 무게 K
N,K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

# 무게(i)별 value만 저장
dp = [0]*(K+1)
for w, v in a:
    for i in range(K, w-1, -1): # 최대 무게부터 해당 물건 무게까지 거꾸로 비교
        dp[i] = max(dp[i-w] + v, dp[i])
print(dp[K])