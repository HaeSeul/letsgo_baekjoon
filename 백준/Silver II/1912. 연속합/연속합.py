N = int(input())
lst=list(map(int, input().split()))

dp = [0]*N
dp[0] = lst[0]  # 초기값
for i in range(1,N):
    if dp[i-1] < 0:   # 내 직전에 합이 음수였다면 나부터 다시 더하기
        dp[i] = lst[i]
    else:
        dp[i] = dp[i-1] + lst[i]
print(max(dp))