class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cmp_dict = defaultdict(lambda: 1001)
        for i, v in enumerate(arr2):
            cmp_dict[v] = i
        return sorted(arr1, key=lambda x: (cmp_dict[x], x))