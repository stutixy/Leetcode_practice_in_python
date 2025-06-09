class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        n = len(nums)
        for i in range(len(nums)):
            size = n - i  
            if size <= nums[i] and size > prev:
                return size
            prev = nums[i]
        return -1

   

        
            