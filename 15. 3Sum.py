class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = n-1
            sum = float('inf')
            while l< r:
                sum  = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l > 0 and nums[l] == nums[l-1] and l<r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
                
                
                    
 
        return res

        