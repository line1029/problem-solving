from sys import stdin, stdout

stdin.readline()
words = map(str.strip, stdin.readlines())
for word in words:
    length = len(word)
    if word == word[::-1]:
        stdout.write(f"1 {length//2 + 1}\n")
        continue
    for i in range(length//2):
        if word[i] != word[length - i - 1]:
            stdout.write(f"0 {i + 1}\n")
            break