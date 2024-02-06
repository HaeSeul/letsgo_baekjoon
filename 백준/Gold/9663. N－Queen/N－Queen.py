def cross(n):
    for i in range(n):
        # 같은 행에 있거나     대각선에 있을 때
        if (a[n]==a[i]) or (abs(n-i)==abs(a[n]-a[i])):
            return True
    return False

def dfs(n):
    global cnt
    if n==N:    # N개 뽑았다면 종료
        cnt += 1
        return

    for j in range(N):
        if not v[j]:            # 선택하지 않은 열 중에
            a[n] = j            # 현재 행에 넣어보기
            if not cross(n):    # 가능한 위치인 경우
                v[j] = 1        # 해당 열 선택
                dfs(n+1)        # 다음 행 탐색
                v[j] = 0

N = int(input())
v = [0]*N   # 열 중복체크
a = [0]*N   # index : 행(n), 값 : 열(j)
cnt = 0
# 0개 뽑은 상태 (row=0)
dfs(0)
print(cnt)