import sys
input = sys.stdin.readline

def get(node, start, end, left, right):
    if right < start or end < left : return 0
    if left <= start and end <= right : return tree[node]
    mid = (start + end) // 2
    left_child = get(node*2, start, mid, left, right)
    right_child = get(node*2+1, mid+1, end, left, right)
    return left_child + right_child

def update(node, start, end, idx, diff):
    if idx < start or end < idx : return
    tree[node] += diff
    if start == end: return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, diff)
    update(node*2+1, mid+1, end, idx, diff)
    return

N = int(input())
arr = list(enumerate(map(int, input().split())))    # (인덱스, 값)
arr.sort(key=lambda x:x[1])     # 값 기준 정렬
tree = [0] * 4*N
swap = 0

# 작은 값부터 트리에 채워넣으며 해당 인덱스 뒤에 해당 값보다 작은 수가 몇 개인지 세기
for i in range(N):
    swap += get(1, 0, N-1, arr[i][0]+1, N-1)
    update(1, 0, N-1, arr[i][0], 1)
print(swap)