N = int(input())
T = []
P = []
for _ in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0]*(N+1)

for i in range(N):
    for j in range(i + T[i], N+1):  # i번째 상담 이후 가능한 상담
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]
print(dp[-1])