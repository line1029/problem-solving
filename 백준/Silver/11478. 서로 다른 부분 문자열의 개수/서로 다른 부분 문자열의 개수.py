word = input()
n = len(word)
s = set()
for i in range(n):
    for j in range(i+1, n+1):
        s.add(word[i:j])
print(len(s))