def find(x):
    # len의 처음과 마지막 요소부터 시작
    i,j = 0, len(a)-1

    # i,j가 역전되기 전까지 실행
    while i<=j:
        # i,j의 중앙값 갱신
        m = (i+j)//2
        if x == a[m]:
            return 1
        elif x < a[m]:
            j = m-1
        else:
            i = m+1

    return 0

# b가 a에 존재하는지 확인
N=int(input())
a=list(map(int, input().split()))
a.sort()

M=int(input())
b=list(map(int, input().split()))

# a 에서 b의 요소들이 있는지 확인
for i in b:
    print(find(i))