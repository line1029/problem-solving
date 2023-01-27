from sys import stdin
n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
leng = len(arr)
start_idx = 0
cnt = 0
step = 1
robots = [0]*leng
robots_loc = set()
cur_robot = 0
while cnt < k:
    start_idx -= 1
    start_idx %= leng
    end_idx = start_idx+n-1
    end_idx %= leng

    if robots[end_idx]:
        robots[end_idx] = 0
    
    for i in range(n-1):
        cur_idx = (end_idx-i)%leng
        if robots[cur_idx]:
            next_idx = (cur_idx+1)%leng
            if robots[next_idx] or not arr[next_idx]:
                continue
            robots[next_idx] = 1
            robots[cur_idx] = 0
            arr[next_idx] -= 1
            if not arr[next_idx]:
                cnt += 1
            if next_idx == end_idx:
                robots[next_idx] = 0
    
    if not robots[start_idx] and arr[start_idx]:
        robots[start_idx] = 1
        arr[start_idx] -= 1
        if not arr[start_idx]:
            cnt += 1

    if cnt >= k:
        break
    step += 1
print(step)