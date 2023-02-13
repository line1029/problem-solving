n = input()
if int(n) >= 777777:
    print(777777)
    exit()
s = []
cnt = 0
for idx, num in enumerate(n):
    if num < "4":
        while s and s[-1] == "4":
            s.pop()
            cnt += 1
        if s:
            s.pop()
            s.append("4")
            s += ["7"]*(cnt + 1)
        else:
            s = ["7"]*cnt
        break
    elif num == "4":
        s.append("4")
    elif num < "7":
        s.append("4")
        break
    elif num == "7":
        s.append("7")
    else:
        s.append("7")
        break
s += ["7"]*(len(n) - idx - 1)
print("".join(s))