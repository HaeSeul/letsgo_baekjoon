N=int(input())  # 계단 개수
stairs = [0]+list(int(input()) for _ in range(N))

dp=[0]*301            # 각 층에 올 수 있는 경우 중 큰 값 저장
dp[1] = stairs[1]               # 첫 계단은 1가지 방법만 존재
if N>=2:
    dp[2] = stairs[1]+stairs[2]     # 첫번째를 거쳐가야 최대
if N>=3:
    dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])   # 1칸->2칸 vs 2칸->1칸

for i in range(4, N+1):
    # N-3 -> N-1 -> N (1칸 오르기 전엔 무조건 2칸 오르기)
    a=dp[i-3]+stairs[i-1]+stairs[i]
    # N-2 -> N
    b=dp[i-2]+stairs[i]
    # 마지막에 1칸 오른 것과 2칸 오른 것 중 큰 것 선택
    dp[i] = max(a,b)

print(dp[N])