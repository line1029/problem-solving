from sys import stdin, stdout
stdin.readline()
arr = stdin.readlines()
arr.sort(key=lambda x: int(x.split()[0]))
stdout.write("".join(arr))
