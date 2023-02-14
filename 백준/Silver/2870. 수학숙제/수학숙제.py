from sys import stdin, stdout
import re
stdin.readline()
ans = sorted(map(int, re.findall("\d+", stdin.read())))
stdout.writelines(f"{i}\n" for i in ans)