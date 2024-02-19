v = [[0]*7 for _ in range(7)]
ans = 'Valid'
si,sj = 0,0     # 시작좌표
ei,ej = 0,0     # 최종좌표

for i in range(1,37):
    x = input()
    ci,cj = ord(x[0])-64, int(x[1])
    if i==1:
        si,sj = ei,ej = ci,cj
    else:
        # 나이트의 이동이 아닌 경우
        isNight = 0
        for di,dj in ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)):
            ni,nj = ei+di, ej+dj
            if not (1<=ni<7 and 1<=nj<7):   continue
            if (ci,cj) == (ni,nj):
                isNight = 1
                break
        if not isNight:
            ans = 'Invalid'
            break

        ei,ej = ci,cj

    if not v[ci][cj]:
        v[ci][cj] = i
    else:   # 방문했던 곳 또 방문
        ans = 'Invalid'
        break

# 마지막에 시작점으로 돌아오지 못함
isValid = 0
for di,dj in ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)):
    ni,nj = ei+di, ej+dj
    if not (1<=ni<7 and 1<=nj<7):   continue
    if v[ni][nj]==1:
        isValid = 1
        break
if not isValid:
    ans = 'Invalid'

print(ans)