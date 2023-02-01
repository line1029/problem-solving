from collections import Counter
s = Counter(input().upper()).most_common()
if len(s) > 1:
    if s[0][1] == s[1][1]:
        print("?")
    else:
        print(s[0][0])
else:
    print(s[0][0])
