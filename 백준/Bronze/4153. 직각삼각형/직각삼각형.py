from sys import stdin
tri = stdin.readlines()
tri.pop()
tri = list(map(lambda x: sorted(map(int, x.split())), tri))
ans = ("right" if i[0]**2 + i[1]**2 == i[2]**2 else "wrong" for i in tri)
print("\n".join(ans))