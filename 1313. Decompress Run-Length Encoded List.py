class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            val = nums[i+1]
            freq = nums[i]
            while freq > 0:
                result.append(val)
                freq -= 1
        return result
        