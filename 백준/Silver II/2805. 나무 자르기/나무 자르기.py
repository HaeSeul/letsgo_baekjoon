def count_tree(m):
    h = 0
    for i in tree:
        # 기준값보다 큰 값만 연산
        if i >= m:
            h += i - m  # 나무와 m의 차이 누적
    return h

# 최소 높이 M
N,M=map(int, input().split())
tree=list(map(int, input().split()))
ans=0

# 시작 : 0, 끝 : 최대 길이 나무
s,e = 0, max(tree)
while s<=e:
    m=(s+e)//2
    h = count_tree(m)
    if h >= M:       # 최소 높이보다 커지면 시작점 갱신
        # 현재 m일 때 최소 M을 만족하면서 max값인 것
        ans = max(ans, m)
        s = m+1
    else:            # 조건 만족하는 나무 연산 후 최소 높이를 만족하지 못하면 끝 값 갱신
        e = m-1
print(ans)