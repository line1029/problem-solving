def solution(code):
    res = []
    mode = 0
    for idx, char in enumerate(code):
        if char == "1":
            mode = not mode
            continue
        if not mode and not idx&1:
            res.append(char)
        elif mode and idx&1:
            res.append(char)
    return "".join(res) if res else "EMPTY"