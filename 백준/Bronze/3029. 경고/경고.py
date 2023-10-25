a = 0
for i in map(int, input().split(":")):
    a *= 60
    a += i
b = 0
for i in map(int, input().split(":")):
    b *= 60
    b += i
if b > a:
    c = b - a
else:
    c = 86400 - a + b
s = c%60
c //= 60
m = c%60
h = c//60
print(f"{h:02}", f"{m:02}", f"{s:02}", sep=":")