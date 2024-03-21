T = int(input())
for _ in range(T):
    N = int(input())
    cmd = list(input().split())

    F = [['r' for _ in range(3)] for _ in range(3)]
    B = [['o' for _ in range(3)] for _ in range(3)]
    U = [['w' for _ in range(3)] for _ in range(3)]
    D = [['y' for _ in range(3)] for _ in range(3)]
    L = [['g' for _ in range(3)] for _ in range(3)]
    R = [['b' for _ in range(3)] for _ in range(3)]

    for change, dr in cmd:

        u_row0, u_row2 = [i for i in U[0]], [i for i in U[2]]
        u_col0 = list(map(list, zip(*U)))[0]
        u_col2 = list(map(list, zip(*U)))[2]

        d_row0, d_row2 = [i for i in D[0]], [i for i in D[2]]
        d_col0 = list(map(list, zip(*D)))[0]
        d_col2 = list(map(list, zip(*D)))[2]

        f_row0, f_row2 = [i for i in F[0]], [i for i in F[2]]
        f_col0 = list(map(list, zip(*F)))[0]
        f_col2 = list(map(list, zip(*F)))[2]

        b_row0, b_row2 = [i for i in B[0]], [i for i in B[2]]
        b_col0 = list(map(list, zip(*B)))[0]
        b_col2 = list(map(list, zip(*B)))[2]

        l_row0, l_row2 = [i for i in L[0]], [i for i in L[2]]
        l_col0 = list(map(list, zip(*L)))[0]
        l_col2 = list(map(list, zip(*L)))[2]

        r_row0, r_row2 = [i for i in R[0]], [i for i in R[2]]
        r_col0 = list(map(list, zip(*R)))[0]
        r_col2 = list(map(list, zip(*R)))[2]


        # 주사위 돌리는 면 기준으로 전개도 재배치
        if change == 'F':
            if dr == '+':
                F  = list(map(list, zip(*F[::-1])))
                for i in range(3):
                    L[i][2] = d_row0[i]
                    D[0][i] = r_col0[2-i]
                    R[i][0] = u_row2[i]
                    U[2][i] = l_col2[2-i]
            else:
                F = list(map(list, zip(*F)))[::-1]
                for i in range(3):
                    L[i][2] = u_row2[2-i]
                    D[0][i] = l_col2[i]
                    R[i][0] = d_row0[2-i]
                    U[2][i] = r_col0[i]

        elif change == 'B':
            if dr == '+':
                B = list(map(list, zip(*B[::-1])))
                for i in range(3):
                    R[i][2] = d_row2[2-i]
                    U[0][i] = r_col2[i]
                    L[i][0] = u_row0[2-i]
                    D[2][i] = l_col0[i]
            else:
                B = list(map(list, zip(*B)))[::-1]
                for i in range(3):
                    R[i][2] = u_row0[i]
                    U[0][i] = l_col0[2-i]
                    L[i][0] = d_row2[i]
                    D[2][i] = r_col2[2-i]

        elif change == 'L':
            if dr == '+':
                L = list(map(list, zip(*L[::-1])))
                for i in range(3):
                    U[i][0] = b_col2[2-i]
                    F[i][0] = u_col0[i]
                    D[i][0] = f_col0[i]
                    B[i][2] = d_col0[2-i]
            else:
                L = list(map(list, zip(*L)))[::-1]
                for i in range(3):
                    U[i][0] = f_col0[i]
                    B[i][2] = u_col0[2-i]
                    D[i][0] = b_col2[2-i]
                    F[i][0] = d_col0[i]

        elif change == 'R':
            if dr == '+':
                R = list(map(list, zip(*R[::-1])))
                for i in range(3):
                    U[i][2] = f_col2[i]
                    B[i][0] = u_col2[2-i]
                    D[i][2] = b_col0[2-i]
                    F[i][2] = d_col2[i]
            else:
                R = list(map(list, zip(*R)))[::-1]
                for i in range(3):
                    U[i][2] = b_col0[2-i]
                    B[i][0] = d_col2[2-i]
                    D[i][2] = f_col2[i]
                    F[i][2] = u_col2[i]

        elif change == 'U':
            if dr == '+':
                U = list(map(list, zip(*U[::-1])))
                B[0],L[0],F[0],R[0] = l_row0, f_row0, r_row0, b_row0

            else:
                U = list(map(list, zip(*U)))[::-1]
                B[0], L[0], F[0], R[0] = r_row0, b_row0, l_row0, f_row0

        elif change == 'D':
            if dr == '+':
                D = list(map(list, zip(*D[::-1])))
                F[2], R[2], B[2], L[2] = l_row2, f_row2, r_row2, b_row2
            else:
                D = list(map(list, zip(*D)))[::-1]
                F[2], R[2], B[2], L[2] = r_row2, b_row2, l_row2, f_row2

    for i in range(3):
        for j in range(3):
            print(U[i][j], end='')
        print()