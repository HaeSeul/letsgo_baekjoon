import sys
from collections import deque
N = int(sys.stdin.readline().strip())
q = deque(x for x in range(1, N + 1))
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q[0])