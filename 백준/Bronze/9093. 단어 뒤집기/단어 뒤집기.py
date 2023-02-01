from sys import stdin, stdout
stdin.readline()
cases = map(lambda x: " ".join(map(lambda y: y[::-1], x.split())), stdin.read().splitlines())
stdout.write("\n".join(cases))