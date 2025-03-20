class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [heights[i] for i in range(len(heights))]
        expected.sort()
        outofOrder = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                outofOrder += 1
        return outofOrder
        