lst = list(input())
s = []
ans = 0
for i in range(len(lst)):
    if lst[i] == '(':
        s.append(lst[i])
    else:
        s.pop()
        if lst[i-1]=='(':
            ans += len(s)
        else:
            ans += 1
print(ans)