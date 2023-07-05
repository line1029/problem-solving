from math import sqrt, gcd
def main():
    # nx^2 + (n+1)x - (n+2) = 0
    # x = (-(n+1) +- sqrt(5n^2 + 10n + 1)) / 2n
    n = int(input())
    t = int(sqrt(5*n**2 + 10*n + 1))
    if t**2 != 5*n**2 + 10*n + 1:
        print(-1)
        exit()
    nu_a = t - n - 1
    nu_b = - t - n - 1
    g_a = gcd(nu_a, n*2)
    g_b = gcd(nu_b, n*2)
    nu_a //= g_a
    nu_b //= g_b
    de_a = 2*n//g_a
    de_b = 2*n//g_b
    if n%(de_a*de_b):
        print(-1)
        exit()
    n //= (de_a*de_b)
    print(de_a, -nu_a, n*de_b, -n*nu_b)
main()