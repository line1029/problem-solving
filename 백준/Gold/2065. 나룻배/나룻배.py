from sys import stdin
input = stdin.readline
m, t, n = map(int, input().split())
left, right = [], []
ans = [0]*n
cur_time = 0
at_left = True
passenger_on_board = 0
for i in range(n):
    time, station = input().split()
    if station == "left":
        left.append((int(time), i))
    else:
        right.append((int(time), i))
left.sort(reverse=True)
right.sort(reverse=True)

while left or right:
    if at_left:
        while left and left[-1][0] <= cur_time and passenger_on_board < m:
            time, idx = left.pop()
            ans[idx] = cur_time + t
            passenger_on_board += 1
        if not passenger_on_board:
            if (left and right and left[-1][0] <= right[-1][0]) or not right:
                cur_time = left[-1][0]
                while left and left[-1][0] <= cur_time and passenger_on_board < m:
                    time, idx = left.pop()
                    ans[idx] = cur_time + t
                    passenger_on_board += 1
            else:
                cur_time = max(right[-1][0], cur_time)
    else:
        while right and right[-1][0] <= cur_time and passenger_on_board < m:
            time, idx = right.pop()
            ans[idx] = cur_time + t
            passenger_on_board += 1
        if not passenger_on_board:
            if (right and left and right[-1][0] <= left[-1][0]) or not left:
                cur_time = right[-1][0]
                while right and right[-1][0] <= cur_time and passenger_on_board < m:
                    time, idx = right.pop()
                    ans[idx] = cur_time + t
                    passenger_on_board += 1
            else:
                cur_time = max(left[-1][0], cur_time)
    passenger_on_board = 0
    cur_time += t
    at_left = not at_left
print("\n".join(map(str, ans)))