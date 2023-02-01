from sys import stdin, stdout
stdin.readline()
arr = sorted(list(map(int, stdin.read().split())))
stdout.write('\n'.join(map(str,arr)))