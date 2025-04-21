class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right) // 2
            if nums[left] <= nums[mid] and nums[mid] < nums[right]:
                right = mid
            elif nums[left] > nums[mid]:
                right = mid
            else:
                left = mid +1
            
        return nums[left]






        