class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [1_000_000_000] * (n + 1)
        dp[0] = 0
        for i in range(n):
            cur_shelf_height = 0
            cur_remain_width = shelfWidth
            for j in range(i, -1, -1):
                if cur_remain_width - books[j][0] < 0:
                    break
                cur_shelf_height = max(cur_shelf_height, books[j][1])
                cur_remain_width -= books[j][0]
                dp[i + 1] = min(dp[i + 1], dp[j] + cur_shelf_height)
        return dp[n]
        