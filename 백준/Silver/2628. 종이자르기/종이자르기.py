width, height = map(int, input().split())
n = int(input())
row = [0, height]
col = [0, width]
for i in range(n):
    a, b = map(int, input().split())
    if a==0:
        row.append(b)
    else:
        col.append(b)
row = sorted(row)
col = sorted(col)

mx_h = mx_w = 0
for i in range(1, len(row)):
    h = row[i]-row[i-1]
    mx_h = max(mx_h, h)
for j in range(1, len(col)):
    w = col[j]-col[j-1]
    mx_w = max(mx_w, w)

print(mx_h*mx_w)