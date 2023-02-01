from sys import stdin, stdout
stdin.readline()
arr = map(lambda x: str(sum(map(int, x.split()))), stdin.read().splitlines())
stdout.write("\n".join(arr))
