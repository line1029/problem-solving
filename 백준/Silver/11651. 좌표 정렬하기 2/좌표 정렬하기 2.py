from sys import stdin, stdout
def order(x):
    x = x.split()
    return int(x[1]), int(x[0])
stdin.readline()
arr = stdin.read().splitlines()
arr.sort(key=order)
stdout.write("\n".join(arr))