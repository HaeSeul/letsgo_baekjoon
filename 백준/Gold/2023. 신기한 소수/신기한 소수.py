def prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def dfs(n,num):
    if not prime(num):
        return

    if n==N:
        print(tmp[-1])
        return

    for i in odd:
        x = num*10+i
        tmp.append(x)
        dfs(n+1, x)
        tmp.pop()


N=int(input())
prime_num=[2,3,5,7]
odd=[1,3,5,7,9]
tmp=[]

if N==1:
    print(*prime_num, sep='\n')
else:
    for i in range(len(prime_num)):
        dfs(1,prime_num[i])