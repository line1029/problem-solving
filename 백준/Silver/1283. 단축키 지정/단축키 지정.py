from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    operations = [i.strip() for i in stdin.readlines()]
    s = 0
    res = []
    for op in operations:
        idx = None
        words = op.split()

        for i, word in enumerate(words):
            if word and not (s & (1 << (ord(word[0].lower()) - 65))):
                s |= 1 << (ord(word[0].lower()) - 65)
                idx = sum((len(x) for x in words[:i]), i)
                res.extend([op[:idx], "[", op[idx], "]", op[idx + 1 :], "\n"])
                break
        else:
            for idx, char in enumerate(op):
                if char == " ":
                    continue
                if not (s & (1 << (ord(char.lower()) - 65))):
                    s |= 1 << (ord(char.lower()) - 65)
                    res.extend([op[:idx], "[", op[idx], "]", op[idx + 1 :], "\n"])
                    break
            else:
                res.extend([op, "\n"])

    stdout.write("".join(res))


main()
