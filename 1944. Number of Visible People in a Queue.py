class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                res[stack[-1]] += 1
                stack.pop()
            if stack:
                res[stack[-1]] += 1
            stack.append(i)

        return res
