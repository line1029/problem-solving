from sys import stdin, stdout
from operator import itemgetter
n = int(stdin.readline())
arr = [list(map(int, i.split())) for i in stdin.read().splitlines()]
arr.sort(key=itemgetter(1, 0))
stdout.write("\n".join(f"{i[0]} {i[1]}" for i in arr))