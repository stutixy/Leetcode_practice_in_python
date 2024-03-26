class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])
        k = len(result)
        for i in range(len(result)):
            nums[i]=result[i]
        return k
        