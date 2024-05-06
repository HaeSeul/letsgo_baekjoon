def pre(root):
    if root != '.':
        print(root, end='')
        pre(t[root][0])
        pre(t[root][1])

def inorder(root):
    if root != '.':
        inorder(t[root][0])
        print(root, end='')
        inorder(t[root][1])

def post(root):
    if root != '.':
        post(t[root][0])
        post(t[root][1])
        print(root, end='')

N = int(input())
t = dict()

for _ in range(N):
    n, l, r = input().split()
    t[n] = [l, r]

pre('A')
print()
inorder('A')
print()
post('A')