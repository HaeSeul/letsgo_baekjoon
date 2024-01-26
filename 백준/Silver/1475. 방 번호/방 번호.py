N = list(map(int, input()))
lst = [0]*10
for i in N:
    lst[i] += 1
a, b = divmod(lst[6]+lst[9], 2)
lst[6] = a+b
print(max(lst[:9]))