from sys import stdin
def prefix(s):
    cur = trie
    for char in s:
        if "*" in cur:
            return True
        if char not in cur:
            return False
        cur = cur[char]
    return True

def insert(s):
    cur = trie
    for char in s:
        if char not in cur:
            cur[char] = dict()
        cur = cur[char]
    cur["*"] = True

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    trie = dict()
    flag = False
    for _ in range(n):
        s = stdin.readline().strip()
        if prefix(s):
            flag = True
        insert(s)
    if flag:
        print("NO")
    else:
        print("YES")
