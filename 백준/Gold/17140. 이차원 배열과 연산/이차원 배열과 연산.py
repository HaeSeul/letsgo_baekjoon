from collections import defaultdict

row,col,key = map(int, input().split())
row -= 1
col -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
while True:
    # 종료조건
    if len(arr) > row and len(arr[0]) > col and arr[row][col] == key:
        break
    if time >= 100:
        time = -1
        break

    # R/C 연산 결정
    op = 0 if len(arr) >= len(arr[0]) else 1

    if op == 1:     # L 연산인 경우 90도 뒤집고 시작
        arr = list(map(list, zip(*arr[::-1])))

    time += 1
    mx_len = 0
    for r in range(len(arr)):
        target = arr.pop(0)

        # 각 숫자의 개수 세기
        dic = defaultdict(int)
        for t in target:
            if t==0: continue
            dic[t] += 1

        # 적은 것부터, 작은 수부터 정렬
        table = []
        for k,v in dic.items():
            table.append((k,v))
        table.sort(key=lambda x:(x[1], x[0]))

        # 하나의 리스트로 합쳐주기
        tmp = []
        for t in table:
            for tt in t:
                tmp.append(tt)
        mx_len = max(mx_len, len(tmp))
        arr.append(tmp)

    # 길이 차이만큼 0 더해주기
    for i in range(len(arr)):
        r = arr[i]
        while len(r) < mx_len:
            r.append(0)
        if len(r) > 100:
            arr[i] = r[:100]

    if op == 1:     # L 연산이었다면 되돌려주기
        arr = list(map(list, zip(*arr)))

print(time)