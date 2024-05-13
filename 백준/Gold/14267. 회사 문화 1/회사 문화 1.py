import sys
input = sys.stdin.readline

'''
직속 child ++하면 아래 children ++
직속 parent 것을 내거에 더하기
'''

N,M = map(int, input().split())
parent = [0]+list(map(int, input().split()))
score = [0 for _ in range(N+1)]

for _ in range(M):
    i, w = map(int, input().split())
    score[i] += w

for i in range(2, N+1):
    score[i] += score[parent[i]]

print(*score[1:])