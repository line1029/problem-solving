from sys import stdin
from collections import deque, defaultdict
def get_next_node(num):
    L = (num*10)%10000 + num//1000
    R = num//10 + (num%10)*1000
    D = (num*2)%10000
    S = (num-1)%10000
    return D, S, L, R


def get_previous_node(num, depth_arr, cur_depth):
    cur_depth -= 1
    if num%2 == 0:
        if depth_arr[num//2] == cur_depth:
            return num//2, "D"
        elif depth_arr[(num+10000)//2] == cur_depth:
            return (num+10000)//2, "D"
    if depth_arr[(num+1)%10000] == cur_depth:
        return (num+1)%10000, "S"
    if depth_arr[num//10 + (num%10)*1000] == cur_depth:
        return num//10 + (num%10)*1000, "L"
    if depth_arr[(num*10)%10000 + num//1000] == cur_depth:
        return (num*10)%10000 + num//1000, "R"


def bfs(start, end, depth_arr):
    cur_depth = 0
    depth_arr[start] = 0
    q = deque([start])
    while q:
        cur_depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            for nex in get_next_node(cur):
                if depth_arr[nex] == -1:
                    depth_arr[nex] = cur_depth
                    if nex == end:
                        return
                    q.append(nex)


for _ in range(int(stdin.readline())):
    start, end = map(int, stdin.readline().split())
    depth_arr = [-1]*10000
    bfs(start, end, depth_arr)
    cur_depth = depth_arr[end]
    cur_node = end
    ans = []
    while cur_node != start:
        nex_node, path = get_previous_node(cur_node, depth_arr, cur_depth)
        cur_depth -= 1
        cur_node = nex_node
        ans.append(path)
    print("".join(reversed(ans)))