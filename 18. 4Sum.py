class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1

                while left < right:
                    sum = nums[left] + nums[right] + nums[i] + nums[j]
                    if sum == target:
                        results.append([nums[left] , nums[right] , nums[i] , nums[j]])
                        left += 1
                        while left < len(nums) and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                    elif sum > target:
                        right -= 1
                    else:
                        left += 1

        return results