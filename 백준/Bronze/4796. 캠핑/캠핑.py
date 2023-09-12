from sys import stdin
def main():
    for idx, (l, p, v) in enumerate(map(lambda x: map(int, x.split()), stdin.read().splitlines()), 1):
        if not p:
            break
        q, r = divmod(v, p)
        print(f"Case {idx}: {q*l + min(l, r)}")
main()