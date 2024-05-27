import sys
input = sys.stdin.readline

from math import ceil, log2

def make_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    make_tree(node*2, start, mid)   # left child
    make_tree(node*2+1, mid+1, end) # right child
    tree[node] = tree[node*2] * tree[node*2 + 1] % num

def get(node, start, end, left, right):
    # 노드가 범위 밖일 때
    if right < start or end < left: return 1

    # 노드가 범위 안일 때
    if left <= start and end <= right: return tree[node]

    # 노드가 범위 일부만 걸칠 때
    mid = (start + end) // 2
    left_child  = get(node*2, start, mid, left, right)
    right_child = get(node*2+1, mid+1, end, left, right)
    return left_child * right_child % num

def update(node, start, end, idx, x):
    # 범위밖
    if idx < start or end < idx: return

    if start == end:
        tree[node] = x
        return

    mid = (start + end) // 2
    update(node*2, start, mid, idx, x)
    update(node*2+1, mid+1, end, idx, x)
    tree[node] = tree[node*2] * tree[node*2+1] % num
    return

N,M,K = map(int, input().split())
num = 1000000007
arr = [int(input()) for _ in range(N)]
h = ceil(log2(N))
tree = [0] * (2 ** (h+1))   # 노드 15개, 배열은 노드+1(1부터 시작)
make_tree(1, 0, N-1)

for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a==1:
        update(1, 0, N-1, b-1, c)
    else:
        print(get(1, 0, N-1, b-1, c-1))