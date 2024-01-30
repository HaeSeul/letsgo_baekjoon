import sys
N = int(sys.stdin.readline().strip())
stk = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    if 'top'==s:
        print(stk[-1] if stk else -1)
    elif 'size'==s:
        print(len(stk))
    elif 'empty'==s:
        print(0 if stk else 1)
    elif 'pop'==s:
        print(stk.pop() if stk else -1)
    else:
        s, n = s.split()
        stk.append(n)