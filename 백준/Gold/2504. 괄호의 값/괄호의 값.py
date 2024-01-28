def solve(a):
    s = []
    ans = 0
    cnt = 1
    for i in range(len(a)):
        item = a[i]
        if item=='(':
            s.append(item)
            cnt *= 2
        elif item=='[':
            s.append(item)
            cnt *= 3
        elif item==')':
            if len(s)==0 or s[-1]=='[':
                return 0
            if a[i-1]=='(':
                ans += cnt
            s.pop()
            cnt//=2
        else:
            if len(s)==0 or s[-1]=='(':
                return 0
            if a[i-1]=='[':
                ans += cnt
            s.pop()
            cnt//=3
    if s:
        return 0
    else:
        return ans

a = list(input())
print(solve(a))