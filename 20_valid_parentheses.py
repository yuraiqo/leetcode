class Solution:
    def isValid(self, s: str) -> bool:
        brackets: dict[str, str] = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack: list[str] = []
        for b in s:
            if b not in brackets:
                stack.append(b)
                continue
            if not stack or stack[-1] != brackets[b]:
                return False
            stack.pop()
        return not stack
