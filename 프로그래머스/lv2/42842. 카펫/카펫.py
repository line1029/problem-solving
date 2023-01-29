def solution(brown, yellow):
    """
    2x + 2y - 4 = brown
    (x-2)(y-2) = yellow
    wlog, x >= y
    (x-2)(-x+(brown/2)) = yellow
    x^2 - (2 + (brown/2))x + yellow + brown = 0
    x = (2 + (brown/2) + sqrt((2 + (brown/2))^2 - 4(yellow+brown)))/2
    y = brown/2 - x + 2
    """
    from math import sqrt
    x = (2 + (brown//2) + sqrt((2 + (brown//2))**2 - 4*(yellow+brown)))//2
    y = (brown//2) - x + 2
    return [x, y]