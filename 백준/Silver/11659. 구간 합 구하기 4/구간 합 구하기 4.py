N,M = map(int, input().split())
lst = [0]+list(map(int, input().split()))

for i in range(1, N+1):
    lst[i] += lst[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(lst[j]-lst[i-1])