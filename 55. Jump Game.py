class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        jump = 0
        for i in range(len(nums)):
            if jump<0:
                return False
            if jump < nums[i]:
                jump = nums[i]
            jump -= 1
        

        
        return True