from sys import stdin
for _ in range(int(stdin.readline())):
    word = list(stdin.readline().strip())
    n = len(word)
    for i in range(n - 2, -1, -1):
        if word[i] < word[i + 1]:
            break
    else:
        print("".join(word))
        continue
    for j in range(n - 1, i, -1):
        if word[j] > word[i]:
            break
    word[i], word[j] = word[j], word[i]
    word[i + 1:] = reversed(word[i + 1:])
    print("".join(word))