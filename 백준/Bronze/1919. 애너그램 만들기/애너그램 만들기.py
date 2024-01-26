a = list(input())
b = list(input())
for i, v in enumerate(a):
    if v in b:
        a[i] = b[b.index(v)] = 0
print(len(a)+len(b)-a.count(0)-b.count(0))