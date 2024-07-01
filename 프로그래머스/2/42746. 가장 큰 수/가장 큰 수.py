def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: (x*4)[:4], reverse=True)
    if numbers[0][0] == "0":
        return "0"
    return "".join(numbers)