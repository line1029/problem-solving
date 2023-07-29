from sys import stdin
def main():
    n, f = int(stdin.readline()), int(stdin.readline())
    r = n%f
    n0 = n%100
    if n0 >= r:
        n0 -= r
        while n0 >= f:
            n0 -= f
    else:
        n0 += f - r
    print(f"{n0:02}")
    
main()