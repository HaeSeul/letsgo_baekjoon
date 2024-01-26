def vps(lst):
    s = []
    for i in lst:
        if i == '(':
            s.append(i)
        else:
            if len(s)!= 0 and s[-1] == '(':
                s.pop()
            else:
                return 'NO'
    if len(s) != 0:
        return 'NO'
    else:
        return 'YES'

T = int(input())
for _ in range(T):
    lst = list(input())
    print(vps(lst))