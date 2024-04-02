def check(row):
    global ans

    lst = arr[row]
    make = [0 for _ in range(N)]

    for r in range(2):
        if r==1:
            lst = lst[::-1]     # 정방향 한 번, 역방향 한 번씩

        for i in range(N - 1):
            if (lst[i] - lst[i + 1]) > 1:
                return False            # 활주로 길이차 1 초과

            elif (lst[i] - lst[i + 1]) == 1:
                j = i + 1
                bridge = []
                while j < N and lst[i + 1] == lst[j] and len(bridge) < X:
                    if lst[i + 1] == lst[j]:
                        if r==0:    # 순방향
                            bridge.append(j)
                        else:       # 역방향
                            bridge.append(N-1-j)
                    j += 1

                if len(bridge) >= X:        # 활주로 건설
                    for b in bridge:
                        if make[b]:
                            return False    # 활주로 겹침
                        make[b] = 1

                else:
                    return False        # 다리 길이 부족

    return True


T = int(input())
for tc in range(1, T+1):
    N,X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for row in range(N):
        if check(row):
            ans += 1

    arr = list(map(list, zip(*arr[::-1])))
    for row in range(N):
        if check(row):
            ans += 1

    print(f'#{tc} {ans}')