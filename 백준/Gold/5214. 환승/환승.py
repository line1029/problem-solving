import io, os
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, k, m = map(int, input().split())
hypertubes = []
stations = [[] for _ in range(n + 1)]
tubes_visited = [-1]*m
stations_visited = [-1]*(n + 1)
stations_visited[1] = 1
q = deque()
ends = set()
for i in range(m):
    hypertubes.append(list(map(int, input().split())))
    for s in hypertubes[-1]:
        stations[s].append(i)
        if s == 1:
            q.append(i)
            tubes_visited[i] = 1
        if s == n:
            ends.add(i)
if not ends:
    print(-1)
    exit()
for i in range(2, 1002):
    if not q:
        break
    for _ in range(len(q)):
        cur_tube = q.popleft()
        for cur_station in hypertubes[cur_tube]:
            if stations_visited[cur_station] == -1:
                stations_visited[cur_station] = i
                for nex_tube in stations[cur_station]:
                    if tubes_visited[nex_tube] == -1:
                        tubes_visited[nex_tube] = i
                        q.append(nex_tube)
print(stations_visited[n])
