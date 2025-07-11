class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        longest = 0
        target = len(nums)-1
        
        for i in range(1, len(nums)):
            if nums[i] == abs(nums[i-1]):
                nums[i] = 0-nums[i]
        nums.sort()
        for r in range(len(nums)):
            if nums[r] <= 0:
                l += 1
                continue
            while l < r and nums[r] - nums[l] > target:
                l += 1
            longest = max(longest, r-l+1)
        
        return len(nums)-longest 