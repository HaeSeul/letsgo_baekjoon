import sys
input = sys.stdin.readline

def make_tbl(ptn):
    tb = [0]*sz
    i = 0
    for j in range(1, sz):
        while i>0 and ptn[i] != ptn[j]:
            i = tb[i-1]
        if ptn[i] == ptn[j]:
            i += 1
            tb[j] = i
    return tb

S,K = input().split()
sz, K = len(S), int(K)
tb = make_tbl(S)

# 한번은 그냥 붙이고 K-1번은 겹치는 부분 빼고 붙이기
print(sz + (sz-tb[-1])*(K-1))