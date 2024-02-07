import sys
input = sys.stdin.readline

'''
연속되는 친구 5명 관계 존재 여부
M개 관계 조합 중 연속되는 4개 나열 
'''

def dfs(n, s):
    global ans
    if len(tmp)==5:    # 5명이 연속되면 1
        ans=1
        return

    # 현재(s)와 연속되는 i 탐색
    for i in adj[s]:
        if not v[i]:
            v[i]=1
            tmp.append(i)
            dfs(n+1, i)
            tmp.pop()
            v[i]=0


# N명, M개 관계
N,M=map(int, input().split())
adj = [[] for _ in range(N)]    # N명의 관계 저장
for _ in range(M):
    v1,v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
ans = 0

for person in range(N):
    v = [0]*N   # 중복 없이 뽑기
    # 각 person부터 시작
    v[person] = 1
    tmp = [person]
    dfs(0, person)    # 0명 뽑은 상태, person부터 시작
    v[person] = 0
    if ans:
        break

print(ans)