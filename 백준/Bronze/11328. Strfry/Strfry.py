N = int(input())
for _ in range(N):
    a, b = input().split()
    if len(a)==len(b):
        v = [0]*len(b)
        for i in range(len(a)):
            for j in range(len(b)):
                if v[j] == 0 and a[i]==b[j]:
                    v[j]=1
                    break
        if 0 in v:
            print('Impossible')
        else:
            print('Possible')
    else:
        print('Impossible')