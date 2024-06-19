class Solution:
    def divide(self, a: int, b: int) -> int:
        if not a:
            return 0
        is_plus = (a < 0) == (b < 0)
        a, b = abs(a), abs(b)
        ans = 0
        while a >= b:
            q = 1
            while a > (b << q):
                q += 1
            q -= 1
            ans += (1 << q)
            a -= (b << q)
        if not is_plus:
            ans = -ans
        if ans == (1 << 31):
            ans -= 1
        return ans
        