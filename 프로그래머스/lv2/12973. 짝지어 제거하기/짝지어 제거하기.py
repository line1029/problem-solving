def solution(s):
    q = []
    for char in s:
        if q and q[-1] == char:
            q.pop()
        else:
            q.append(char)
    if q:
        return 0
    return 1
        