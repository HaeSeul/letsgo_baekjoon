N = int(input())
arr=[list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준 정렬
arr.sort(key= lambda x:(x[1],x[0]))
# 첫번째 포함하고 시작
cnt=1
e=arr[0][1]

for i in range(1,N):
    # 이전 회의 끝나는 시간 이후인 경우
    if e <= arr[i][0]:
        e=arr[i][1]
        cnt+=1
print(cnt)