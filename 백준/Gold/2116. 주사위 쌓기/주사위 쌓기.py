from sys import stdin, stdout


def swap(arr: list):
    arr[3], arr[4], arr[5] = arr[5], arr[3], arr[4]


def get_max(top_idx: int, arr: list):
    return max(arr[(top_idx + 1) % 6], arr[(top_idx + 2) % 6], arr[(top_idx + 4) % 6], arr[(top_idx + 5) % 6])


def main():
    n = int(stdin.readline())
    first = list(map(int, stdin.readline().split()))
    swap(first)
    dice = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
    max_score = 0
    for die in dice:
        swap(die)
    for i, x in enumerate(first):
        score = get_max(i, first)
        for die in dice:
            idx = die.index(x)
            score += get_max(idx, die)
            x = die[(idx + 3) % 6]
        max_score = max(max_score, score)
    stdout.write(f"{max_score}")


main()
