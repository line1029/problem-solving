from sys import stdin
import heapq
n = int(stdin.readline())
def get_dist(a, b):
    a, b = planets[a], planets[b]
    return min(abs(i - j) for i, j in zip(a, b))
planets = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
idx_y = list(range(n))
idx_y.sort(key=lambda x: planets[x][1])
inv_y = [0]*n
for i, num in enumerate(idx_y):
    inv_y[num] = i
idx_z = list(range(n))
idx_z.sort(key=lambda x: planets[x][2])
inv_z = [0]*n
for i, num in enumerate(idx_z):
    inv_z[num] = i
visited = [0]*n
pq = [(0, 0)]
ans = 0
while pq:
    dist, cur = heapq.heappop(pq)
    if visited[cur]:
        continue
    visited[cur] = 1
    ans += dist
    if cur > 0 and not visited[cur - 1]:
        heapq.heappush(pq, (get_dist(cur, cur - 1), cur - 1))
    if cur < n - 1 and not visited[cur + 1]:
        heapq.heappush(pq, (get_dist(cur, cur + 1), cur + 1))
    cur_y = inv_y[cur]
    if cur_y > 0 and not visited[idx_y[cur_y - 1]]:
        heapq.heappush(pq, (get_dist(cur, idx_y[cur_y - 1]), idx_y[cur_y - 1]))
    if cur_y < n - 1 and not visited[idx_y[cur_y + 1]]:
        heapq.heappush(pq, (get_dist(cur, idx_y[cur_y + 1]), idx_y[cur_y + 1]))
    cur_z = inv_z[cur]
    if cur_z > 0 and not visited[idx_z[cur_z - 1]]:
        heapq.heappush(pq, (get_dist(cur, idx_z[cur_z - 1]), idx_z[cur_z - 1]))
    if cur_z < n - 1 and not visited[idx_z[cur_z + 1]]:
        heapq.heappush(pq, (get_dist(cur, idx_z[cur_z + 1]), idx_z[cur_z + 1]))
print(ans)
