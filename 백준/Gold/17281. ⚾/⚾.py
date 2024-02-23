# [ 1 ] 9명의 순열 중 4번째가 1번 선수인 경우
def permute(n):
    global mx
    # 8명을 뽑고 3번째에 0번 끼워넣기
    if n==8:
        # 각 순열의 max 점수 갱신
        mx = max(mx, play(orders[:3]+[0]+orders[3:]))
        return

    for i in range(1,9):
        if not v[i]:
            v[i] = 1
            orders.append(i)
            permute(n+1)
            orders.pop()
            v[i] = 0

# [ 2 ] 현재 타자 순서대로 play 했을 때의 점수 리턴
def play(order):
    cnt, i = 0, 0
    for n in range(N):   # 이닝
        out = 0
        a,b,c=0,0,0
        while True:
            x = arr[n][order[i]]    # n번째 이닝 / order[i]번째 선수의 결과
            if x == 0:
                out += 1
                if out > 2:
                    i = (i+1)%9     # 아웃된 타자 다음부터 시작
                    break
            elif x == 1:
                cnt += c
                a,b,c = 1,a,b
            elif x == 2:
                cnt += b+c
                a,b,c = 0,1,a
            elif x == 3:
                cnt += a+b+c
                a,b,c = 0,0,1
            else:  # 홈런
                cnt += a+b+c+1
                a,b,c = 0,0,0
            i = (i+1)%9             # 이닝 끝나도 타자 순서 유지
    return cnt

N=int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [1,0,0,0,0,0,0,0,0]     # 9명 중 1번 타자 제외
orders = []
mx = 0
permute(0)                  # 0명 뽑은 상태부터 시작
print(mx)