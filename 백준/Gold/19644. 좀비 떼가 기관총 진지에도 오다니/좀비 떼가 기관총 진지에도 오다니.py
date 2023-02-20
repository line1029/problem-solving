from sys import stdin
l = int(stdin.readline())
ml, mk = map(int, stdin.readline().split())
c = int(stdin.readline())
if c >= l:
    print("YES")
    exit()
zombies = enumerate(map(int, stdin.read().splitlines()))
prefix_sum_bomb = [0]
for idx, z in zombies:
    if idx < ml:
        damage = (idx + 1 - prefix_sum_bomb[idx])*mk
        if damage < z:
            if not c:
                print("NO")
                exit()
            c -= 1
            prefix_sum_bomb.append(prefix_sum_bomb[-1] + 1)
        else:
            prefix_sum_bomb.append(prefix_sum_bomb[-1])
    else:
        damage = (ml - prefix_sum_bomb[idx] + prefix_sum_bomb[idx - ml])*mk
        if damage < z:
            if not c:
                print("NO")
                exit()
            c -= 1
            prefix_sum_bomb.append(prefix_sum_bomb[idx] + 1)
        else:
            prefix_sum_bomb.append(prefix_sum_bomb[idx])
print("YES")