def solution(s):
    ans = [0, 0]
    while s != "1":
        ones = s.count("1")
        zeros = len(s) - ones
        ans[0] += 1
        ans[1] += zeros
        s = bin(ones)[2:]
    return ans
        
    