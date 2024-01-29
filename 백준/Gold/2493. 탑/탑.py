N = int(input())
lst = list(map(int, input().split()))
s = []      # (탑순서, 탑높이) 저장
ans = []

for i in range(N):
    while s and lst[i] > s[-1][1]:
        s.pop()         # 지금 탑보다 낮은 탑들 삭제
    if s:       # 삭제 후 남아있다면 s[-1]의 탑 선택
        ans.append(s[-1][0])
    else:
        ans.append(0)
    s.append((i+1, lst[i]))
print(*ans)