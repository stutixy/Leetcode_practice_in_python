class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i+1
            right =  len(nums)-1
            targetSum = 0-nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left < right:
                if nums[left] + nums[right] == targetSum:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < targetSum:
                    left += 1
                else:
                    right -= 1
        return result
                    






        