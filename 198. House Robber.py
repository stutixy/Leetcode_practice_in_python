class Solution:
    def rob(self, nums: List[int]) -> int:
        lastNonAdjacentValue = 0
        lastAdjacentValue = 0
        current = 0
        for num in nums:
           current = max(num + lastNonAdjacentValue, lastAdjacentValue)
           lastNonAdjacentValue = lastAdjacentValue
           lastAdjacentValue = current
        return current

        