from sys import stdin
n, m = map(int, stdin.readline().split())
dna = stdin.read().splitlines()
s = "ACGT"
ans = []
hamming_distance = 0
for j in range(m):
    acgt = [0]*4
    for i in range(n):
        if dna[i][j] == "A":
            acgt[0] += 1
        elif dna[i][j] == "C":
            acgt[1] += 1
        elif dna[i][j] == "G":
            acgt[2] += 1
        else:
            acgt[3] += 1
    idx = acgt.index(max(acgt))
    ans.append(s[idx])
    hamming_distance += n - acgt[idx]
print("".join(ans), hamming_distance, sep="\n")