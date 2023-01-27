def solution(s):
    print(s.split(" "))
    arr = list(map(lambda x: x[0].upper() + x[1:].lower() if x else x, s.split(" ")))
    return " ".join(arr)