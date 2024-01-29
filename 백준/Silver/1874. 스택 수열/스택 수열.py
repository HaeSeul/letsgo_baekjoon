N = int(input())
s = []
ans=[]
j=1
for _ in range(N):
    i = int(input())
    while j<=i:         # i가 될 때까지 j push
        s.append(j)
        ans.append('+')
        j+=1
    if s and i==s[-1]:
        s.pop()
        ans.append('-')
    else:               # i가 s[-1]보다 작아서
        print('NO')     # stack 아래에 쌓여있는 경우
        break
else:                   # break되지 않은 경우
    print(*ans, sep='\n')