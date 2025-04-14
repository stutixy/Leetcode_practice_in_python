class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if left > i+1 and nums[left] == nums[left-1] and left < right:
                    left += 1
                    continue
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right  -= 1
                else:
                    left += 1
        return res


        


        


