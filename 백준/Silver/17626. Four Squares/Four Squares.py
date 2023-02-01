from itertools import product
n = int(input())
cnt = dict([[1, set(i**2 for i in range(1, 224))]])
if n in cnt[1]:
    print(1)
    exit()
def make_sum_of_squares(num):
    tmp = set()
    for x, y in product(cnt[num-1], cnt[1]):
        if x + y <= 50000:
            tmp.add(x + y)
    return tmp

for i in range(2, 4):
    cnt[i] = make_sum_of_squares(i)
    if n in cnt[i]:
        print(i)
        exit()
print(4)
