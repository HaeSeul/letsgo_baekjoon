dir = ((0,1),(-1,0),(0,-1),(1,0))   # 시계90으로 생성 => 반대로 돌아야함
N = int(input())
arr = [[0]*101 for _ in range(101)]
ans = 0
for _ in range(N):
    j,i,d,g = map(int, input().split())
    lst = [d]
    arr[i][j] = 1
    i,j = i+dir[d][0], j+dir[d][1]  # 0세대 우선 이동
    arr[i][j] = 1

    for _ in range(g):  # 세대만큼 반복
        new = []
        for cd in lst[::-1]:  # lst의 뒤에서부터 방향 바꿔가며 추가 (lst 길이만큼 반복)
            nd = (cd + 1) % 4
            i,j = i+dir[nd][0], j+dir[nd][1]    # 갱신을 i,j 그대로 해줘야 끝점 계속 갱신됨
            new.append(nd)
            arr[i][j] = 1
        lst += new          # 드래곤 연장

# 만들어진 정사각형 개수세기
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans += 1
print(ans)