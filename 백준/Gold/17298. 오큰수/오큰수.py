N = int(input())
lst = list(map(int, input().split()))[::-1]
stk = []
ans = []
for i in lst:
    # stk이 있는 경우: 현재 숫자보다 작거나 같은 stk[-1] 없애기
    while stk and i >= stk[-1]:
        stk.pop()

    # stk이 빈 경우 : 지금까지 숫자 중 최대 or 맨 뒤
    if not stk:
        ans.append(-1)
    else:               # stk에 남은 게 있는 경우
        ans.append(stk[-1])
    stk.append(i)       # stk에 자신 추가
print(*ans[::-1])