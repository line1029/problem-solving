from sys import stdin, stdout
num = list(stdin.readline().strip())
num.sort(reverse=True)
stdout.write("".join(num))
