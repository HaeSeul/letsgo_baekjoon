def cal(p):
    ans = A[0]
    for i in range(1,N):
        if p[i-1]==op[0]:       # 덧셈
            ans += A[i]
        elif p[i-1]==op[1]:     # 뺄셈
            ans -= A[i]
        elif p[i-1]==op[2]:     # 곱셈
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
        # [ 2 ] 각 순열 식일 때의 값 구하기
        ans = cal(p)
        mn = min(mn, ans)
        mx = max(mx, ans)
        return
    for i in range(4):
        if v[i] < cmd[i]:
            v[i]+=1
            p.append(op[i])
            permute(n+1)
            p.pop()
            v[i]-=1

N = int(input())
A = list(map(int, input().split()))
cmd = list(map(int, input().split()))   # +-*/ : N-1개
op = '+-*/'
mn,mx = 10**9+1, -10**9-1

# [ 1 ] 연산자 순열만들기
p = []
v = [0]*4
permute(0)

print(mx, mn, sep='\n')