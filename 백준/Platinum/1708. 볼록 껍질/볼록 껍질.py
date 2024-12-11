def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) > 0

def convex(points):
    stack = []
    for C in points:
        while len(stack) >= 2:
            A, B = stack[-2], stack[-1]
            if ccw(*A, *B, *C): break
            stack.pop()
        stack.append(C)
    return len(stack)

N = int(input())
points = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], x[1]))
print(convex(points) + convex(points[::-1]) -2)