def dfs(start):
    global mx
    for i in range(start-1, 0 ,-1):
        if i + T[i] < start + 1:
            lst.append(i)
            dfs(i)
            pay = 0
            for e in lst:
                pay += P[e]
            mx = max(mx, pay)
            lst.pop()

N = int(input())
T = [0]
P = [0]
for _ in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)
mx = 0

for i in range(N, 0, -1):
    if i+T[i] <= N+1:
        lst = [i]
        mx = max(mx, P[i])
        dfs(i)

print(mx)