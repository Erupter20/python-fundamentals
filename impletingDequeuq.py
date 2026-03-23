# Write a python code to implement a queue using collectoins.dequeue

from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(30)

# Print the elements
print(' '.join(map(str, dq)))

dq.popleft()
dq.pop()

print(''.join(map(str, dq)))