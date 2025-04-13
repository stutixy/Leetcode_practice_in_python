class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resultLookup = set()
        result = []
        for i in range(len(nums)-2):
            left = i+1
            right =  len(nums)-1
            targetSum = 0-nums[i]
            while left < right:
                if nums[left] + nums[right] == targetSum:
                    possibleSolution = ''.join([str(nums[i]), str(nums[left]), str(nums[right])])
                    if possibleSolution not in resultLookup:
                        result.append([nums[i], nums[left], nums[right]])
                        resultLookup.add(possibleSolution)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < targetSum:
                    left += 1
                else:
                    right -= 1
        return result
                    






        