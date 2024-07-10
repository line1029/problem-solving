class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_ = s[::-1]
        if s == s_:
            return s
        for i in range(1, len(s)):
            if s[:-i] == s_[i:]:
                return s_[:i] + s
        return s_ + s