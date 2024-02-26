def cal(p):
    ans = A[0]
    for i in range(1,N):
        if p[i-1]==0:       # 덧셈
            ans += A[i]
        elif p[i-1]==1:     # 뺄셈
            ans -= A[i]
        elif p[i-1]==2:     # 곱셈
            ans *= A[i]
        else:               # 나눗셈
            if ans<0:
                ans = (ans * (-1) // A[i]) * -1
            else:
                ans //= A[i]
    return ans

def permute(n):
    global mn, mx
    if n==N-1:  # 모든 연산자를 다 뽑은 경우 순열 완성
        # [ 3 ] 각 순열 식일 때의 값 구하기
        ans = cal(p)
        mn = min(mn, ans)
        mx = max(mx, ans)
        return
    for i in range(N-1):
        if not v[i]:
            v[i]=1
            p.append(cmd[i])
            permute(n+1)
            p.pop()
            v[i]=0

N = int(input())
A = list(map(int, input().split()))
cmd = list(map(int, input().split()))   # +-*/ : N-1개
mn,mx = 10**9, -10**9

# [ 1 ] 연산자를 숫자로 개수만큼 치환하기
for i in range(4):
    x = cmd.pop(0)
    cmd += [i]*x

# [ 2 ] 연산자 순열만들기
p = []
v = [0]*(N-1)
permute(0)

print(mx, mn, sep='\n')