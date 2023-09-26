def main():
    n = int(input())
    s, b = "@"*n, " "*n
    c1 = "\n".join((3*s + b + s) for _ in range(n))
    c2 = "\n".join((s + b + s + b + s) for _ in range(n))
    c3 = c1[::-1]
    print(c1, c2, c2, c2, c3, sep="\n")

main()