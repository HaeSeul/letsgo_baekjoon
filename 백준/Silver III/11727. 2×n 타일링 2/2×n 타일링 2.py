n=int(input())

# n이 하나씩 늘어날 때마다 가능한 경우 확인
dp = [0]*(n+1)
dp[0] = 1   # n==0인 경우 : 안 뽑는 방법 1개
dp[1] = 1   # n==1인 경우 : 2*1 한개
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]*2
print(dp[n]%10007)