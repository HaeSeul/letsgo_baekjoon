ans = 0
for _ in range(int(input())):
    a = list(input())
    s = []
    if len(a)%2==0:
        for i in range(len(a)):
            if len(s)==0:
                s.append(a[i])
            else:
                if s[-1]==a[i]:
                    s.pop()
                else:
                    s.append(a[i])
        if len(s)==0:
            ans += 1
print(ans)