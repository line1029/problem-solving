import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
station_prev = [0]*1000001
station_next = [0]*1000001
def build_station(i, j):
    station_prev[j] = i
    station_next[j] = station_next[i]
    station_prev[station_next[i]] = j
    station_next[i] = j


def cancel_station(i):
    station_next[station_prev[i]] = station_next[i]
    station_prev[station_next[i]] = station_prev[i]


for i in range(n):
    station_prev[arr[i]] = arr[i - 1]
    station_next[arr[i - 1]] = arr[i]
for _ in range(m):
    order, *nums = input().split()
    if order[0] == 66:
        i, j = map(int, nums)
        if order[1] == 78:
            ans.append(f"{station_next[i]}\n")
        else:
            ans.append(f"{station_prev[i]}\n")
            i = station_prev[i]
        build_station(i, j)
    elif order[0] == 67:
        i = int(nums[0])
        if order[1] == 78:
            i = station_next[i]
        else:
            i = station_prev[i]
        ans.append(f"{i}\n")
        cancel_station(i)
os.write(1, ans.build().encode())