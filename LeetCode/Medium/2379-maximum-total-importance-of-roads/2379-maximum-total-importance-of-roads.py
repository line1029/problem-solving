class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        num_of_road = [0]*n
        for a, b in roads:
            num_of_road[a] += 1
            num_of_road[b] += 1
        num_of_road.sort()
        return sum(i*j for i, j in zip(range(1, n + 1), num_of_road))
        