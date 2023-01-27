from sys import stdin, stdout
from collections import deque
n = int(stdin.readline())
queries = stdin.readlines()
q = deque()
def queue(query):
    if query == "pop\n":
        if q:
            stdout.write(f"{q.popleft()}\n")
        else:
            stdout.write("-1\n")
    elif query == "size\n":
        stdout.write(f"{len(q)}\n")
    elif query == "empty\n":
        stdout.write(f"{int(len(q) == 0)}\n")
    elif query == "front\n":
        if q:
            stdout.write(f"{q[0]}\n")
        else:
            stdout.write("-1\n")
    elif query == "back\n":
        if q:
            stdout.write(f"{q[-1]}\n")
        else:
            stdout.write("-1\n")
    else:
        _, num = query.split()
        q.append(num)
for query in queries:
    queue(query)