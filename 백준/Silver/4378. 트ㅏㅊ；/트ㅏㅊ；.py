from sys import stdin
wertyu = dict(zip("1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./ ", "`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,. "))
for s in stdin.read().splitlines():
    res = []
    for char in s:
        res.append(wertyu[char])
    print("".join(res))