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

def dfs(n, arr):
    global mx
    if n==5:
        mx = max(mx, max(map(max, arr)))
        return

    n_arr = [l[::] for l in arr]
    n_arr = push(n_arr)
    dfs(n + 1, n_arr)

    n_arr = list(map(list, zip(*arr)))[::-1]
    n_arr = push(n_arr)
    dfs(n + 1, n_arr)

    n_arr = list(map(list, zip(*arr[::-1])))
    n_arr = push(n_arr)
    dfs(n + 1, n_arr)

    n_arr = [l[::-1] for l in arr]
    n_arr = push(n_arr)
    dfs(n + 1, n_arr)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = -1

dfs(0,arr)
print(mx)