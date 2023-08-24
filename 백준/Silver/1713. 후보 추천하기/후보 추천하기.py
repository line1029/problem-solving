from sys import stdin
def main():
    n = int(stdin.readline())
    m = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    pics = []
    posted = [-1]*101
    for i in range(m):
        if posted[nums[i]] != -1:
            pics[posted[nums[i]]][0] += 1
        else:
            if len(pics) == n:
                j = pics.index(min(pics))
                posted[pics.pop(j)[2]] = -1
                for k in range(j, len(pics)):
                    posted[pics[k][2]] -= 1
            posted[nums[i]] = len(pics)
            pics.append([1, i, nums[i]])
    print(*sorted(i[2] for i in pics))
main()