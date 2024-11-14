from sys import stdin, stdout


def main():
    formular = stdin.readline().strip()
    stack = []
    parenthesis = []
    for idx, char in enumerate(formular):
        if char == "(":
            stack.append(idx)
        elif char == ")":
            parenthesis.append((idx, stack.pop()))
    res = set()
    for bit in range(1, 1 << len(parenthesis)):
        new_formular = list(formular)
        for binary, (idx_1, idx_2) in zip(map(int, bin(bit)[2:].zfill(len(parenthesis))), parenthesis):
            if binary:
                new_formular[idx_1] = new_formular[idx_2] = ""
        res.add("".join(new_formular))
    stdout.write("\n".join(sorted(res)))


main()
