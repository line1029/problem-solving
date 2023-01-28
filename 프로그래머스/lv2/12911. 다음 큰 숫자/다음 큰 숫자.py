def solution(n):
    binary = bin(n)[2:]
    ones = binary.count("1")
    r = len(binary) - 1
    last_zeros = 0
    while r >= 0 and binary[r] == "0":
        last_zeros += 1
        r -= 1
    if last_zeros + ones == len(binary):
        return int("1"+"0"*(last_zeros+1)+"1"*(ones-1), 2)
    last_ones = 0
    while r >= 0 and binary[r] == "1":
        last_ones += 1
        r -= 1
    return int(binary[:r]+"1"+"0"*(last_zeros+1)+"1"*(last_ones-1), 2)
    
    