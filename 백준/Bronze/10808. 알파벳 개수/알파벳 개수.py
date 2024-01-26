s = input()
a = [0]*26
for i in s:
    a[ord(i)-97] += 1
print(*a)