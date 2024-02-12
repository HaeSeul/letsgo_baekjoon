N = int(input())
arr=[list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준 정렬
arr.sort(key= lambda x:(x[1],x[0]))
cnt=end=0

for s,e in arr:
    # 이전 회의 끝나는 시간 이후 시작인 경우
    if end <= s:
        end = e     # 끝나는 시간 갱신
        cnt+=1
print(cnt)