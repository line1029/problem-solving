import sys


def check(word=None):
    if not word:
        return False
    tmp = [True] * 26
    prev = word[0]
    for char in word:
        if char != prev:
            if tmp[ord(char) - 97]:
                tmp[ord(prev) - 97] = False
                prev = char
            else:
                return False
    return True
            

t = int(sys.stdin.readline())
ans = 0
for i in range(t):
    ans += check(sys.stdin.readline().rstrip())

print(ans)
