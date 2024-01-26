N, K = map(int, input().split())
girl = [0]*6
boy = [0]*6
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        girl[Y-1] += 1
    else:
        boy[Y-1] += 1
ans = 0
for i in range(6):
    if girl[i]%K==0:
        ans += girl[i]//K
    else:
        ans += girl[i]//K + 1
    if boy[i]%K==0:
        ans += boy[i]//K
    else:
        ans += boy[i]//K + 1
print(ans)