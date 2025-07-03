class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        if len(nums) == 0:
            return 0

        nums.sort(reverse = True)
        l = 0
        mini = float('inf')
        for r in range(k-1, len(nums)):
            mini = min(mini, nums[l]-nums[r])
            l += 1
        return mini


        