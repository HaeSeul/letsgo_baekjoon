def solve(a):
    s = []
    for i in a:
        if i not in ('(',')','[',']'):
            continue
        if len(s)!=0 and ((s[-1]=='(' and i==')') or (s[-1] == '[' and i == ']')):
            s.pop()
        else:
            s.append(i)
    if len(s) == 0:
        return 'yes'
    else:
        return 'no'
while True:
    a = list(input())
    if a[0]=='.':
        break
    print(solve(a))