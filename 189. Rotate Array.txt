class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k% size
        nums.reverse()

        right = k-1
        left = 0
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        
        left = k
        right = size -1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        return nums

        

        
