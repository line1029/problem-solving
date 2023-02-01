arr = [-1] * 26
for i, s in enumerate(input()):
    if arr[ord(s) - 97] == -1:
        arr[ord(s) - 97] = i
print(" ".join(map(str, arr)))