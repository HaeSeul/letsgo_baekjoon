def solve():
    cnt = 0
    # 계속 정렬하며 앞의 두 값을 비교
    while True:
        if snow[0] > 1440:
            return -1
        if len(snow)==1:
            return snow[0]

        # 큰 값부터 정렬
        snow.sort(reverse=True)

        # 남은 눈이 없을 때
        if snow[0]==0:
            break

        snow[0] -= 1
        # 뒤에 뺄 것이 남아있다면 빼주기
        if snow[1] > 0:
            snow[1] -= 1

        cnt += 1
        if cnt>1440:
            return -1
    return cnt


N=int(input())
snow = list(map(int, input().split()))

print(solve())