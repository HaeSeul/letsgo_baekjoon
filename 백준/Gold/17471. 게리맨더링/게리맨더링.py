import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque


def cal(lst):
    num = len(lst)

    # 길이가 1인 경우 1 리턴
    if num == 1:    return 1

    q = deque([lst[0]])
    v = [0] * (N+1)
    v[lst[0]] = 1
    while q:
        c = q.popleft()
        for i in adj[c]:
            if i not in lst: continue
            if v[i]: continue
            v[i] = 1
            q.append(i)
    # lst의 모든 요소가 연결되어 있는지
    return sum(v) == num


def check(a,b):
    global mn
    if cal(a) and cal(b):  # 연결되어 있다면 최소값 갱신
        sm_a = sum(population[x] for x in a)
        sm_b = sum(population[x] for x in b)
        mn = min(mn, abs(sm_a - sm_b))


def combination(n, k, s):
    if n==k:    # k명 뽑은 경우
        b = [x for x in range(1, N+1) if x not in a]
        # 각 선거구가 서로 연결되어 있는지 확인
        check(a,b)
        return
    for i in range(s, N+1):
        a.append(i)
        combination(n+1,k,i+1)
        a.pop()


N = int(input())
population = [0]+list(map(int, input().split()))
adj = defaultdict(set)

for n in range(1, N+1):
    num, *l = map(int, input().split())
    adj[n] = l

mn = 10e7
a = []
b = []
for k in range(1, N // 2 + 1):
    combination(0, k, 1)

if mn==10e7:
    print(-1)
else:
    print(mn)