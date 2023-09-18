print("\n".join(f"Distances: {' '.join(map(lambda x: str((ord(x[1]) - ord(x[0]))%26), zip(*input().split())))}" for _ in range(int(input()))))
