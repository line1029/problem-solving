from functools import cmp_to_key
def compare(x:str, y:str):
    if x + y > y + x:
        return -1
    return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    if not int(numbers[0]):
        return "0"
    return "".join(numbers)