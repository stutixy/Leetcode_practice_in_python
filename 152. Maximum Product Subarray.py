class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxMin = [[] for i in range(len(nums))]
        maxProduct = nums[0]

        if nums[0] != 0:
            maxMin[0].append(nums[0])
            maxMin[0].append(nums[0])
        else:
            maxMin[0].append(1)
            maxMin[0].append(1)

        for i in range(1, len(nums)):
            if nums[i] != 0:
                maxMin[i].append(max(maxMin[i-1][0] * nums[i], maxMin[i-1][1] * nums[i], nums[i]))
                maxMin[i].append(min(maxMin[i-1][0] * nums[i], maxMin[i-1][1] * nums[i], nums[i]))
                maxProduct = max(maxProduct, maxMin[i][0])
            else:
                maxMin[i].append(1)
                maxMin[i].append(1)
                maxProduct = max(maxProduct, 0)
        return maxProduct
            


    