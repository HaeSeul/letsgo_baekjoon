from collections import deque

def bfs(s):
    v = set()
    v.add(s)
    q = deque([(s, [])])

    while q:
        c, cal = q.popleft()
        if c==t:
            # 가장 먼저 완성되는 조합 return
            return cal

        # (-)는 어차피 0이 되기 때문에 연산에서 제외
        for i in ('*', '+'):
            n = eval('c'+i+'c')
            if 0<=n<=mx and n not in v:
                v.add(n)
                q.append((n, cal+[i]))

        if c!=0:
            n = 1   # eval('c/c') = 1
            if 0 <= n <= mx and n not in v:
                v.add(n)
                q.append((n, cal+['/']))
    return -1

s,t = map(int, input().split())
mx = 10**9

if s==t:
    print(0)
else:
    ans = bfs(s)
    if ans==-1:
        print(ans)
    else:
        print(''.join(ans))