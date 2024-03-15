def right(arr):
    # 오른쪽으로 옮기기
    for i in range(N):
        turn = [0] * N

        # 행의 뒤에서 두번째 것부터 시작
        for j in range(len(arr) - 2, -1, -1):
            if arr[i][j] == 0: continue
            idx = j

            while True:
                if idx > N - 2: break  # 맨 끝에 도달하면 끝

                # 내 옆이 나와 같고 지금 턴에서 바꾸지 않았다면 합치기
                if arr[i][idx + 1] and arr[i][idx] == arr[i][idx + 1] and not turn[idx + 1]:
                    turn[idx + 1] = 1
                    arr[i][idx + 1] *= 2
                    arr[i][idx] = 0
                    break
                # 내 뒤에 다른 숫자가 있다면 끝
                if arr[i][idx + 1]: break

                # 숫자 옮기기
                arr[i][idx + 1] = arr[i][idx]
                arr[i][idx] = 0
                idx += 1
    return arr

def up(arr):
    # 위로 올리기
    arr = list(map(list, zip(*arr[::-1])))
    arr = right(arr)
    for _ in range(3):
        arr = list(map(list, zip(*arr[::-1])))
    return arr

def down(arr):
    arr = list(map(list, zip(*arr)))
    arr = right(arr)
    arr = list(map(list, zip(*arr)))
    return arr

def left(arr):
    for i in range(N):
        arr[i] = arr[i][::-1]
    arr = right(arr)
    for i in range(N):
        arr[i] = arr[i][::-1]
    return arr


def dfs(n, arr):
    global mx
    if n==5:    # 5번 반복하면 끝
        for l in arr:
            mx = max(mx, *l)
        return

    new_arr = [list(l) for l in arr[::]]

    for d in range(4):
        # 배열 돌리기
        if d==0:
            new_arr = right(new_arr)
        elif d==1:
            new_arr = down(new_arr)
        elif d==2:
            new_arr = left(new_arr)
        else:
            new_arr = up(new_arr)
        dfs(n+1, new_arr)
        new_arr = [list(l) for l in arr[::]]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
dfs(0, arr)
print(mx)