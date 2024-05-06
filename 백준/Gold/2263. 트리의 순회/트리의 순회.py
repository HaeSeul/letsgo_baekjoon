import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def pre(in_s, in_e, post_s, post_e):
    # 재귀 종료
    if (in_s > in_e) or (post_s > post_e): return

    # post의 마지막 노드 = root
    p = post[post_e]
    print(p, end=' ')

    # root 중심으로 inorder에서 left, right 개수 구하기
    left = pos[p] - in_s
    right = in_e - pos[p]

    # 각 left, right 서브트리 순회
    pre(in_s, in_s + left-1, post_s, post_s + left-1)
    pre(in_e - right+1, in_e, post_e - right, post_e-1)

N = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
pos = [0]*(N+1)

for i in range(N):
    pos[inorder[i]] = i

pre(0, N-1, 0, N-1)