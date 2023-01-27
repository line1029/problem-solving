from sys import stdin, stdout
stdin.readline()
pss = list(map(lambda x: x.strip(), stdin.readlines()))
def is_valid(s):
    st = 0
    for char in s:
        if char == "(":
            st += 1
        else:
            st -= 1
        if st < 0:
            return "NO"
    if st > 0:
        return "NO"
    return "YES"
ans = (is_valid(s) for s in pss)
stdout.write("\n".join(ans))