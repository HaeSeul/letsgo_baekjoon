def dfs(s):
    global ans
    # 종료조건 : 합이 S이고 a가 비어있지 않을 때
    if sum(a) == S and a:
        ans += 1
        #return   -> return하게 되면 뒤에 0이 왔을 때 포함하지 못함

    # N개 정수 개수만큼 반복하며
    for i in range(s, N):
        a.append(lst[i])
        dfs(i+1)
        a.pop()

# N개 정수로 이루어진 수열 중 크기가 양수인 부분수열의 합이 S인 경우
N,S = map(int, input().split())
lst = list(map(int, input().split()))

a = []
ans = 0

# lst의 0번째부터 시작
dfs(0)
print(ans)