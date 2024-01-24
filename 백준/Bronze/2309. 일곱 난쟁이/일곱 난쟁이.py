a = [int(input()) for _ in range(9)]
a.sort()
sm = sum(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a.count(0) == 2:
            continue
        if sm - a[i] - a[j] == 100:
            a[i] = a[j] = 0
            break
for j in a:
    if j != 0:
        print(j)