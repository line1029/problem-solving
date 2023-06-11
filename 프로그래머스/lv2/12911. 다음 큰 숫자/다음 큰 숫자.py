def solution(n):
    binary = f"{n:b}"
    ones = binary.count("1")
    pointer = len(binary) - 1
    last_zeros = 0
    while pointer >= 0 and binary[pointer] == "0":
        last_zeros += 1
        pointer -= 1
    if last_zeros + ones == len(binary):
        return int("1"+"0"*(last_zeros+1)+"1"*(ones-1), 2)
    last_ones = 0
    while pointer >= 0 and binary[pointer] == "1":
        last_ones += 1
        pointer -= 1
    return int(binary[:pointer]+"1"+"0"*(last_zeros+1)+"1"*(last_ones-1), 2)
    
    