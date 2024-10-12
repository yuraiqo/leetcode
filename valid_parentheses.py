class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for ch in s:
            if ch not in brackets:
                stack.append(ch)
                continue
            if not stack or stack[-1] != brackets[ch]:
                return False
            stack.pop()
        return not stack
