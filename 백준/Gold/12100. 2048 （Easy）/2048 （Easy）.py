from collections import deque

def push(arr):
    # 왼쪽으로 밀기
    for r in range(N):
        row = deque()
        for c in range(N):
            if arr[r][c] != 0:  # 0 제외하고 deque에 담기
                row.append(arr[r][c])
        lst = []
        while row:
            if len(row) >= 2:
                if row[0] == row[1]:
                    lst.append(row.popleft()*2)
                    row.popleft()
                else:
                    lst.append(row.popleft())
            else:
                lst.append(row.popleft())
        lst += [0] * (N-len(lst))
        arr[r] = lst
    return arr

# 위로밀기 (반시계 90 -> 시계 90)
def push_up(arr):
    arr = list(map(list, zip(*arr)))[::-1]
    arr = push(arr)
    arr = list(map(list, zip(*arr[::-1])))
    return arr

# 아래로밀기 (시계 90 -> 반시계 90)
def push_down(arr):
    arr = list(map(list, zip(*arr[::-1])))
    arr = push(arr)
    arr = list(map(list, zip(*arr)))[::-1]
    return arr

# 오른쪽으로밀기 (전치)
def push_right(arr):
    arr = [l[::-1] for l in arr]
    arr = push(arr)
    arr = [l[::-1] for l in arr]
    return arr

def dfs(n, arr):
    global mx
    if n==5:
        mx = max(mx, max(map(max, arr)))
        return

    n_arr = [l[::] for l in arr]
    for d in range(4):
        if d==0:    # 왼
            n_arr = push(n_arr)
        elif d==1:  # 아
            n_arr = push_down(n_arr)
        elif d==2:  # 오
            n_arr = push_right(n_arr)
        else:       # 위
            n_arr = push_up(n_arr)
        dfs(n + 1, n_arr)
        n_arr = [l[::] for l in arr]


dir = ((0,-1),(-1,0),(0,1),(-1,0))  # 왼아오위

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = -1

dfs(0,arr)
print(mx)