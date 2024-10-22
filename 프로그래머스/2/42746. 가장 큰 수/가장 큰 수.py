def solution(numbers):
    """
    ["3", "34", "33", "32", "343", "3434"]
    -> "3434", "34", "343", "33", "3", "32"
    """
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    if not int(numbers[0]):
        return "0"
    return "".join(numbers)