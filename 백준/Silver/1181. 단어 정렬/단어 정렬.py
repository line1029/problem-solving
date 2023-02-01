from sys import stdin, stdout
arr = list(set(stdin.readlines()[1:]))
arr.sort(key=lambda x: (len(x), x))
stdout.write("".join(arr))