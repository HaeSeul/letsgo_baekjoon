import sys
input = sys.stdin.readline

# 합이 26이 되어야 하는 리스트의 인덱스
l = [[1,3,6,8],[1,4,7,11],[8,9,10,11],[2,3,4,5],[2,6,9,12],[5,7,10,12]]

def check(checklist):
    for i in range(6):
        sm = 0
        for j in range(4):
            sm += checklist[l[i][j]]
        if sm!=26:
            return False
    return True

def print_result(a):
    for i in range(1,13):
        a[i] = chr(a[i]+64)
    print(f'....{a[1]}....')
    print(f'.{a[2]}.{a[3]}.{a[4]}.{a[5]}.')
    print(f'..{a[6]}...{a[7]}..')
    print(f'.{a[8]}.{a[9]}.{a[10]}.{a[11]}.')
    print(f'....{a[12]}....')

def dfs(n):
    global flag
    if n==13:
        if check(lst):
            print_result(lst)
            flag=1
        return

    if flag:    return

    if lst[n]:
        dfs(n+1)
        return

    # 1~12 돌아가며 탐색
    for num in range(1,13):
        if not v[num]:
            v[num]=1
            lst[n]=num
            dfs(n+1)
            lst[n]=0
            v[num]=0


# x->0, 알파벳->숫자로 변경해서 나열
lst=[0]         # 1:A를 맞춰주기 위해 0으로 시작
v = [0] * 13    # 1:A ~ 12:L

for _ in range(5):
    x = input().rstrip()
    for c in x:
        if c=='.':  continue
        elif c=='x':
            lst.append(0)
        else:
            lst.append(ord(c)-64)
            v[ord(c)-64]=1

flag=0
# index 1부터 가능한 모든 경우의 수 탐색
dfs(1)