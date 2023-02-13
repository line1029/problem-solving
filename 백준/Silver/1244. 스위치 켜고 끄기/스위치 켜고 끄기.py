from sys import stdin, stdout
n = int(stdin.readline())
switch = list(map(int, stdin.readline().split()))
k = int(stdin.readline())
students = map(lambda x: map(int, x.split()), stdin.read().splitlines())
for student, num in students:
    if student == 1:
        for i in range(num - 1, n, num):
            switch[i] ^= 1
    else:
        l = r = num - 1
        switch[l] ^= 1
        l -= 1
        r += 1
        while l >= 0 and r < n and switch[l] == switch[r]:
            switch[l] ^= 1
            switch[r] ^= 1
            l -= 1
            r += 1
for idx, state in enumerate(switch):
    if idx%20 == 19:
        stdout.write(f"{state}\n")
    else:
        stdout.write(f"{state} ")