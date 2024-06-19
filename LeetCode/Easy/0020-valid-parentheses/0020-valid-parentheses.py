class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {"{":"}", "(":")","[":"]"}
        for char in s:
            if char in maps:
                stack.append(maps[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True