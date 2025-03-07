class Solution(object):
    def majorityElement(self, nums):
        n= len(nums)
        eMap = {}
        for i in range(n):
            if nums[i] not in eMap:
                eMap[nums[i]] = 0
            eMap[nums[i]] += 1
            if  eMap[nums[i]] > n//2:
                return nums[i]

        