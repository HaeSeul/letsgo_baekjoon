# 회전 4회
type1 = [[[1,0,0,0],[1,1,1,1],[1,0,0,0]],
         [[0,1,0,0],[1,1,1,1],[0,1,0,0]]]
# 회전 2회 + 대칭
type2 = [[[1,0,0,0],[1,1,1,1],[0,0,0,1]],
         [[0,1,0,0],[1,1,1,1],[0,0,1,0]],
         [[1,1,0,0],[0,1,1,0],[0,0,1,1]],
         [[1,1,1,0,0],[0,0,1,1,1]]]
# 회전 4회 + 대칭
type3 = [[[1,0,0,0],[1,1,1,1],[0,1,0,0]],
        [[1,0,0,0],[1,1,1,1],[0,0,1,0]],
        [[1,1,0,0],[0,1,1,1],[0,1,0,0]],
        [[1,1,0,0],[0,1,1,1],[0,0,1,0]],
        [[1,1,0,0],[0,1,1,1],[0,0,0,1]]]
shapes = []     # 총 64개

def flip(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return arr

def rotate90(arr):
    return list(map(list, zip(*arr[::-1])))

for t in type1:
    for _ in range(4):
        shapes.append(t)
        t = rotate90(t)
for t in type2:
    for _ in range(2):
        shapes.append(t)
        t = rotate90(t)
    t = flip(t)
    for _ in range(2):
        t = rotate90(t)
        shapes.append(t)
for t in type3:
    for _ in range(4):
        shapes.append(t)
        t = rotate90(t)
    t = flip(t)
    for _ in range(4):
        t = rotate90(t)
        shapes.append(t)

def check(shape,n,m,R,C):
    # 도형의 모든 부분과 일치하는지 확인
    for r in range(R):
        for c in range(C):
            if shape[r][c]==1 and arr[n+r][m+c]==0:
                return 0
    return 1

def find_loc(shape):
    # arr의 어느 부분에 있는지 찾기
    R,C = len(shape), len(shape[0])
    for n in range(6-R+1):
        for m in range(6-C+1):
            if check(shape,n,m,R,C):
                return 1
    return 0

for _ in range(3):
    ans = 'no'
    arr = [list(map(int, input().split())) for _ in range(6)]
    for shape in shapes:
        if find_loc(shape):
            ans = 'yes'
    print(ans)