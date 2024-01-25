N, M = map(int, input().split())
a = list(map(int, input().split()))
mx = sm = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sm = a[i]+a[j]+a[k]
            if sm>mx and sm<=M:
                mx = sm
print(mx)