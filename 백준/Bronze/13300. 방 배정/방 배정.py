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
    p, v = divmod(girl[i], 2)
    ans += p+v
    p, v = divmod(boy[i], 2)
    ans += p+v
print(ans)