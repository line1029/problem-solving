from sys import stdin, stdout
k = int(stdin.readline())
ineqs = stdin.readline().split()
nums = set(range(10))
candidates = []
def backtracking(ineqs, idx, pattern, left):
    for num in left:
        if ineqs[idx] == "<" and pattern[-1] < num:
            if len(pattern) == k:
                candidates.append(pattern + [num])
            else:
                backtracking(ineqs, idx + 1, pattern + [num], left.difference([num]))
        elif ineqs[idx] == ">" and pattern[-1] > num:
            if len(pattern) == k:
                candidates.append(pattern + [num])
            else:
                backtracking(ineqs, idx + 1, pattern + [num], left.difference([num]))
    
    
for i in range(10):
    backtracking(ineqs, 0, [i], nums.difference([i]))

max_pattern = max(candidates)
min_pattern = min(candidates)
max_num = "".join(map(str, max_pattern))
min_num = "".join(map(str, min_pattern))

print(max_num)
print(min_num)