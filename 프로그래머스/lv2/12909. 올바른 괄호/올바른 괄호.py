def solution(s):
    stack = 0
    for char in s:
        if char == "(":
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    if stack == 0:
        return True
    return False