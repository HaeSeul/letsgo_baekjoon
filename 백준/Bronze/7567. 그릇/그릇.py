a = list(input())
ans = 10
for i in range(1, len(a)):
    if a[i-1]==a[i]:
        ans += 5
    else:
        ans += 10
print(ans)