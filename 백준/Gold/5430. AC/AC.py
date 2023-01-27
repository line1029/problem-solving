from sys import stdin
from collections import deque
def action(query, arr):
    if query.count("D") > len(arr):
        print("error")
        return
    parity = True
    for char in query:
        if char == "R":
            parity = not parity
        else:
            if parity:
                arr.popleft()
            else:
                arr.pop()
    if not parity:
        arr = reversed(arr)
    print(f"[{','.join(map(str, arr))}]")
    return

for _ in range(int(stdin.readline())):
    query = stdin.readline().strip()
    n = int(stdin.readline())
    if n > 0:
        arr = deque(map(int, stdin.readline().strip()[1:-1].split(",")))
    else:
        stdin.readline()
        arr = deque()
    action(query, arr)