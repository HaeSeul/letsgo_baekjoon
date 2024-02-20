import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(s):
    global flag
    if flag:  # b를 만난다면 종료
        return
    for c in adj[s]:       # (동굴,길이)
        if not v[c[0]]:
            tmp.append(c[1])    # 길이 저장
            v[c[0]] = 1         # 동굴 방문
            if c[0] == b:
                flag = 1
            dfs(c[0])
            if flag:    # b를 만난다면 종료
                return
            tmp.pop()
            v[c[0]] = 0


N,a,b = map(int, input().split())
adj = [[] for _ in range(N+1)]
v = [0]*(N+1)
flag = 0    # a->b 경로를 구했는지
sm,mx = 0,0

for _ in range(N-1):
    s,e,d = map(int, input().split())
    adj[s].append((e,d))
    adj[e].append((s,d))

# 한 번 거쳐간 동굴은 돌아가면 안 됨
tmp = []    # 거쳐가는 동굴 경로
v[a] = 1
dfs(a)      # a부터 시작

for dist in tmp:
    sm += dist
    mx = max(mx, dist)
print(sm - mx)