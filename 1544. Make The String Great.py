class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if not stack or stack[-1].swapcase() != s[i]:
                stack.append(s[i])
            elif stack :
                stack.pop()
        return "".join(stack)
        