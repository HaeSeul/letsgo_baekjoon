import sys
input = sys.stdin.readline

def get(node, start, end, left, right):
    # 노드가 범위 밖일 때
    if right < start or end < left: return 0

    # 노드가 범위 안일 때
    if left <= start and end <= right: return tree[node]

    # 노드가 범위 일부만 걸칠 때
    mid = (start + end) // 2
    left_child  = get(node*2, start, mid, left, right)
    right_child = get(node*2+1, mid+1, end, left, right)
    return left_child + right_child

def update(node, start, end, idx, x):
    # 범위 밖이면 끝
    if idx < start or end < idx: return

    if start == end:
        tree[node] = x
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, idx, x)
    update(node * 2 + 1, mid + 1, end, idx, x)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

N,M = map(int, input().split())
arr = [0] * N
tree = [0] * (4*N)

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd:
        update(1, 0, N-1, a-1, b)
        arr[a-1] = b
    else:
        if a > b: a, b = b, a
        print(get(1, 0, N-1, a-1, b-1))