class Solution:
    def jump(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1], nums[i] + i)
        minjump = 0
        i = 0
        while i < len(nums)-1:
            minjump += 1
            i = nums[i]
        return minjump
        